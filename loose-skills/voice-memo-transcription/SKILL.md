---
name: voice-memo-transcription
description: Transcribe voice memos / audio recordings into text so the user can use spoken thoughts as prompts. Triggers when the user shares an audio file path (.m4a, .mp3, .wav, .ogg, .flac, .opus, .webm), mentions "transcribe this", "what does this voice memo say", "voice note", "audio file", or drops a file from their phone's voice memo / WhatsApp voice / iPhone Voice Memos / Recorder app. Tries OpenAI Whisper API first (fast, ~6s for 1-min audio), falls back to local whisper.cpp if installed. Returns a clean transcript with timestamps optional.
---

# Voice Memo Transcription

Convert audio files into transcribed text. Designed for the workflow: speak a thought into your phone → drop the file into Claude Code → use the transcript as a prompt or save to memory.

## When to use

- User says "transcribe this voice memo" / "what does this audio say" / "I recorded a thought"
- User shares a path to an audio file (`.m4a`, `.mp3`, `.wav`, `.ogg`, `.flac`, `.opus`, `.webm`)
- User pastes a path that ends in audio extensions
- WhatsApp voice messages exported as `.opus` or `.ogg`
- iPhone Voice Memos exported as `.m4a`
- Android Recorder app saves as `.m4a` or `.amr`

## Procedure

1. **Locate the file.** Confirm path with `ls -la <path>`. If the user dropped a file in `~/Downloads/` or `~/Desktop/`, use that path directly.

2. **Pick a backend.** Run the transcription script which auto-detects:
   - **Path A: OpenAI Whisper API** (preferred — fast, accurate, ~$0.006/minute). Requires `OPENAI_API_KEY` in env.
   - **Path B: Local whisper.cpp** if `whisper.cpp` binary is on PATH. Slower but free + offline.
   - **Path C: faster-whisper** (Python) if installed. CTranslate2-based, GPU-accelerated.

3. **Run the script:**
   ```bash
   python C:/Users/toner/.claude/skills/voice-memo-transcription/scripts/transcribe.py <audio-file>
   ```
   Or with timestamps:
   ```bash
   python C:/Users/toner/.claude/skills/voice-memo-transcription/scripts/transcribe.py <audio-file> --timestamps
   ```

4. **Return the transcript** in the chat. Don't paraphrase — quote it verbatim.

5. **Then ask** the user: "What do you want to do with it?" Common follow-ups:
   - "Use this as my next prompt" → carry the transcript forward as the request
   - "Save to memory" → use claude-mem or a memory file
   - "Add to Obsidian" → use `mcp__obsidian__obsidian_append_content` to a note
   - "Spawn into a task" → use `mcp__ccd_session__spawn_task` with the transcript as the prompt

## File format support

| Format | Whisper API | whisper.cpp | faster-whisper |
|---|:---:|:---:|:---:|
| .mp3 | ✓ | ✓ | ✓ |
| .m4a | ✓ | ✓ | ✓ |
| .wav | ✓ | ✓ | ✓ |
| .ogg / .opus | ✓ | ✓ (via ffmpeg) | ✓ |
| .flac | ✓ | ✓ | ✓ |
| .webm | ✓ | ✓ (via ffmpeg) | ✓ |
| .amr | converts via ffmpeg first | ✓ | ✓ |

If FFmpeg is not on PATH but the audio is in a non-WAV format, the script will fail with a clear error. FFmpeg was installed earlier in this stack at `C:/Users/toner/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_*/`.

## Language handling

Whisper auto-detects language. For Star Toner workflows, voice memos may be in:
- Spanish (Cádiz, ES) — primary
- English — secondary
- Arabic (occasionally)
- French (when collaborating with father)

If detection is wrong, pass `--lang es` (or `en`, `ar`, `fr`).

## Privacy considerations

⚠️ **OpenAI Whisper API** sends audio to OpenAI servers. Don't use for confidential content. Use local whisper.cpp for sensitive recordings (customer calls, internal strategy, etc.).

## Cost notes

- OpenAI Whisper API: $0.006/minute (~$0.36 per hour of audio)
- Local whisper.cpp: free but ~5-15x slower depending on model size
- For 1-minute voice memos, the API is essentially free and ~6s round-trip

## Failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| `OPENAI_API_KEY not set` | No env var | Set `OPENAI_API_KEY` in shell or `.env`, or install whisper.cpp |
| `ffmpeg: command not found` | FFmpeg missing | `winget install Gyan.FFmpeg` (already installed earlier) |
| Empty transcript | Silent audio / wrong file | Verify audio plays in VLC; check duration |
| Wrong language detected | Mixed-language audio | Pass `--lang <code>` explicitly |
| Cuts off mid-sentence | API timeout on long audio | Split file with `ffmpeg -i in.mp3 -f segment -segment_time 600 chunk_%03d.mp3` |
