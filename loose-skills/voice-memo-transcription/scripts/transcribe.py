#!/usr/bin/env python3
"""
Voice memo transcription with auto-fallback chain:
  1. OpenAI Whisper API (fast, requires OPENAI_API_KEY)
  2. faster-whisper (CTranslate2-based local, requires `pip install faster-whisper`)
  3. whisper.cpp (CLI binary if on PATH)

Usage:
  python transcribe.py <audio-file> [--timestamps] [--lang es|en|ar|fr|auto] [--model tiny|base|small|medium|large]

Outputs raw transcript to stdout. With --timestamps, prints SRT-style segments.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib import request as _req


def transcribe_openai(path: Path, lang: str | None, timestamps: bool) -> str | None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None
    try:
        # Multipart form upload to /v1/audio/transcriptions
        boundary = "----whisper" + os.urandom(8).hex()
        body = []

        def field(name: str, value: str) -> None:
            body.append(f"--{boundary}\r\n".encode())
            body.append(f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode())
            body.append(value.encode())
            body.append(b"\r\n")

        def file_field(name: str, filename: str, data: bytes) -> None:
            body.append(f"--{boundary}\r\n".encode())
            body.append(
                f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'.encode()
            )
            body.append(b"Content-Type: application/octet-stream\r\n\r\n")
            body.append(data)
            body.append(b"\r\n")

        with open(path, "rb") as f:
            data = f.read()

        file_field("file", path.name, data)
        field("model", "whisper-1")
        field(
            "response_format",
            "verbose_json" if timestamps else "text",
        )
        if lang and lang != "auto":
            field("language", lang)

        body.append(f"--{boundary}--\r\n".encode())
        payload = b"".join(body)

        req = _req.Request(
            "https://api.openai.com/v1/audio/transcriptions",
            data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": f"multipart/form-data; boundary={boundary}",
            },
        )
        with _req.urlopen(req, timeout=300) as resp:
            raw = resp.read().decode("utf-8")
        if timestamps:
            obj = json.loads(raw)
            out = []
            for seg in obj.get("segments", []):
                start = seg.get("start", 0)
                end = seg.get("end", 0)
                text = seg.get("text", "").strip()
                out.append(f"[{start:6.2f} → {end:6.2f}] {text}")
            return "\n".join(out)
        return raw.strip()
    except Exception as e:
        print(f"[openai whisper] failed: {e}", file=sys.stderr)
        return None


def transcribe_faster_whisper(path: Path, lang: str | None, timestamps: bool, model: str) -> str | None:
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except ImportError:
        return None
    try:
        m = WhisperModel(model, device="auto", compute_type="auto")
        segs, info = m.transcribe(
            str(path),
            language=None if (not lang or lang == "auto") else lang,
            beam_size=5,
        )
        if timestamps:
            return "\n".join(f"[{s.start:6.2f} → {s.end:6.2f}] {s.text.strip()}" for s in segs)
        return " ".join(s.text.strip() for s in segs).strip()
    except Exception as e:
        print(f"[faster-whisper] failed: {e}", file=sys.stderr)
        return None


def transcribe_whisper_cpp(path: Path, lang: str | None, timestamps: bool, model: str) -> str | None:
    binary = shutil.which("whisper.cpp") or shutil.which("main") or shutil.which("whisper")
    if not binary:
        return None
    # whisper.cpp expects WAV 16kHz; convert via ffmpeg if needed
    tmpwav = path.with_suffix(".tmp.wav")
    try:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            print("[whisper.cpp] ffmpeg not found, cannot convert audio", file=sys.stderr)
            return None
        subprocess.run(
            [ffmpeg, "-y", "-i", str(path), "-ar", "16000", "-ac", "1", str(tmpwav)],
            check=True,
            capture_output=True,
        )
        cmd = [binary, "-m", f"models/ggml-{model}.bin", "-f", str(tmpwav), "-otxt"]
        if lang and lang != "auto":
            cmd += ["-l", lang]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        # whisper.cpp writes <wav>.txt
        txt_path = tmpwav.with_suffix(".wav.txt")
        if txt_path.exists():
            text = txt_path.read_text(encoding="utf-8").strip()
            txt_path.unlink()
            return text
        return result.stdout.strip()
    except Exception as e:
        print(f"[whisper.cpp] failed: {e}", file=sys.stderr)
        return None
    finally:
        if tmpwav.exists():
            tmpwav.unlink()


def main() -> int:
    p = argparse.ArgumentParser(description="Transcribe a voice memo to text.")
    p.add_argument("audio", type=Path, help="Path to audio file")
    p.add_argument("--timestamps", action="store_true", help="Include time-coded segments")
    p.add_argument("--lang", default="auto", help="Language code (es, en, ar, fr) or auto")
    p.add_argument("--model", default="base", help="whisper.cpp / faster-whisper model size")
    args = p.parse_args()

    if not args.audio.exists():
        print(f"ERROR: file not found: {args.audio}", file=sys.stderr)
        return 1

    # Try chain in order
    for fn, name in [
        (lambda: transcribe_openai(args.audio, args.lang, args.timestamps), "OpenAI Whisper API"),
        (lambda: transcribe_faster_whisper(args.audio, args.lang, args.timestamps, args.model), "faster-whisper"),
        (lambda: transcribe_whisper_cpp(args.audio, args.lang, args.timestamps, args.model), "whisper.cpp"),
    ]:
        out = fn()
        if out is not None:
            print(f"# transcribed via {name}", file=sys.stderr)
            print(out)
            return 0

    print(
        "ERROR: no transcription backend available.\n"
        "  Install one of:\n"
        "    1. Set OPENAI_API_KEY env var\n"
        "    2. pip install faster-whisper\n"
        "    3. Install whisper.cpp and put binary on PATH",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
