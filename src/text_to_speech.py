from phonikud_tts import Piper

class TextToSpeech:
    def __init__(self, model_path: str, config_path: str):
        self.model = Piper(model_path, config_path)

    def create(self, text: str):
        return self.model.create(text)