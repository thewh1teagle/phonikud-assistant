# Phonikud-assistant

Local AI assistant in Hebrew with Phonikud

## Setup

1. Open https://console.picovoice.ai/login and continue with Google
2. Set the acess key in `.env` file
3. Install UV https://docs.astral.sh/uv/getting-started/installation
4. Install dependencies

5. Download Phonikud models

```console
wget https://huggingface.co/thewh1teagle/phonikud-onnx/resolve/main/phonikud-1.0.int8.onnx -O phonikud-1.0.int8.onnx
wget https://huggingface.co/thewh1teagle/phonikud-tts-checkpoints/resolve/main/model.onnx -O tts-model.onnx
wget https://huggingface.co/thewh1teagle/phonikud-tts-checkpoints/resolve/main/model.config.json -O tts-model.config.json
```

6. Install dependencies

```console
uv sync
```

7. Run

```console
uv run src/main.py
```