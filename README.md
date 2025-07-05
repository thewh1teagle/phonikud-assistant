# Phonikud-assistant

Local AI assistant in Hebrew with Phonikud ✨

## Setup

1. Open https://console.picovoice.ai/login and continue with Google
2. Set the access key in `.env` file
3. Open https://platform.openai.com/settings and get OpenAI api key, set in `.env`
4. Install UV https://docs.astral.sh/uv/getting-started/installation
5. Download Phonikud models

```console
wget https://huggingface.co/thewh1teagle/phonikud-onnx/resolve/main/phonikud-1.0.int8.onnx -O phonikud-1.0.int8.onnx
wget https://huggingface.co/thewh1teagle/phonikud-tts-checkpoints/resolve/main/shaul.onnx -O tts-model.onnx
wget https://huggingface.co/thewh1teagle/phonikud-tts-checkpoints/resolve/main/model.config.json -O tts-model.config.json
```

STT models

```console
wget https://huggingface.co/ivrit-ai/whisper-large-v3-turbo-ggml/resolve/main/ggml-model.bin
```

6. Install dependencies

```console
uv sync
```

7. Run

note: first time it might take a bit to warm up. you can add prints if you want.

```console
uv run src/main.py
```

## Usage

1. Say `Picovoice!` to wake him up
2. Ask anything and watch the magic! ✨