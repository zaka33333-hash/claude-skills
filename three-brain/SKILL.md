---
name: three-brain
description: Automatically delegates tasks to Codex (GPT-5.5) or Gemini when you say "review with codex", "analyze this video with gemini", "ask all three", or on task failure.
---

This skill implements the "three-brain" auto-router pattern described by Jack Roberts. It keeps Claude as the primary "driver" and code author, but intelligently delegates specific tasks to specialist models.

-   **Driver:** Claude remains the primary interface, the IDE harness, and the one responsible for building, writing, and refactoring code.
-   **Reviewer:** Codex (GPT-5.5) acts as a second brain for code review, quality assurance, and can be called in to "rescue" a failed task.
-   **Senses:** Gemini acts as the eyes and ears, providing long-context analysis for complex inputs like video, audio, and large PDF documents.

### Routing Decision Table

| User phrase / context | Delegate to | Mechanism |
| :--- | :--- | :--- |
| "...review your work with codex", "...Codex reviews that..." | Codex | `/codex:review` with a prompt to review the preceding output for quality, correctness, and security. |
| Prompt includes video, audio, or large PDF files for analysis | Gemini | `/cc-gemini-plugin:gemini` with a prompt to analyze the specified file (e.g., "analyze this video", "summarize this PDF"). |
| "ask all three", "...debate..." between models | All Three | Parallel calls to Claude, Codex, and Gemini with the same prompt, with results compiled into a structured comparison. |
| Claude fails on a task. | Codex | `/codex:rescue` is triggered automatically to attempt a fix. TODO: Transcript is ambiguous. One part says "if it's failed to solve it once", another says "if I fill the simulation twice...I must hand off". Clarify if rescue is on first or second failure. |
| An edit touches a high-risk file path. | Codex | `/codex:adversarial-review` is triggered automatically for a critical security and logic review. |

### Claude Stays Asleep

Claude handles the core development workflow directly. The three-brain skill does not activate for standard requests to:
-   Build new features
-   Write code from scratch
-   Refactor existing code
-   Edit files in non-critical paths
-   Explain concepts or code blocks

### Forced Routes (Adversarial Review)

To ensure maximum security on sensitive parts of a codebase, any edit that touches a file matching the following patterns will automatically trigger a non-optional, critical `/codex:adversarial-review`:

-   `src/auth/**`
-   `**/migrations/**`
-   `**/billing/**`

### Examples

**Example 1: Combined Video Analysis and Code Review**

**Prompt:**
> Hey, there in my downloads is a video from Alexi. I want you to analyze the entire video. I want you to tell me any of the text that appears in the video because the audio is one thing. So, I want to get the transcript, but then I also want the visual overlay. I want to take both of those components and I want to take that and create a beautiful HTML document uh that I can look through and learn from interactively, combining both what's said and what is seen visually. And when that's all done, I just want to make sure that Codex reviews that to make sure there's no mistakes, that it's uh accurate and completely on brief. Thank you.

**Routing:**
1.  The mention of "video" and "analyze the entire video" triggers a call to `/cc-gemini-plugin:gemini` to process the video file, extract the transcript, and perform visual analysis.
2.  Claude uses the structured output from Gemini to generate the HTML document.
3.  The final phrase "make sure that Codex reviews that" triggers a call to `/codex:review` on the generated HTML file.

**Example 2: Simple Code Review**

**Prompt:**
> Awesome. I'd like you to use codeex to review your work.

**Routing:**
1.  The explicit phrase "use codeex to review" triggers a call to `/codex:review` on the code that Claude has just produced.

**Example 3: Multi-Model Debate**

**Prompt:**
> Hey, I want you to use three different models. GPT-5.5, Claude, and Gemini. debate. What is the best social media platform to start a business off in 2026?

**Routing:**
1.  The phrases "use three different models" and "debate" trigger parallel, independent calls to Claude, Codex, and Gemini with the same question.
2.  Claude then synthesizes the three responses into a final verdict.
