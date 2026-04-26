# 🎙️ Real-Time Voice Assistant with LiveKit + LLM

This project implements a real-time voice assistant using LiveKit Agents, integrating speech-to-text (STT), a large language model (LLM), and text-to-speech (TTS) for seamless conversational interaction.

It supports live audio streaming, intelligent responses, and robust retry handling for production-like reliability.

---

##  Features

- Real-time speech input (STT)
- LLM-powered responses (DeepSeek via GitHub Models API)
- Natural speech output (TTS)
- Retry & exponential backoff for API rate limits
- Async architecture for low-latency interaction
- Function calling support (tool integration)

---

## Architecture

User Speech → STT → LLM → TTS → Audio Response

### Components:

- **STT (Speech-to-Text):**
  - Model: `ink-whisper`
  - Converts live audio into text

- **LLM (Language Model):**
  - Model: `deepseek/DeepSeek-V3-0324`
  - Hosted via GitHub Models API
  - Handles reasoning and response generation

- **TTS (Text-to-Speech):**
  - Model: `sonic-3`
  - Converts responses into natural speech

- **VAD (Voice Activity Detection):**
  - Silero VAD for detecting speech segments

---

## Tech Stack

- Python (AsyncIO)
- LiveKit Agents Framework
- DeepSeek LLM (via GitHub Models API)
- Cartesia STT & TTS
- Silero VAD

---
