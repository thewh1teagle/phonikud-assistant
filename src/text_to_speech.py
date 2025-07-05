from phonikud_tts import Piper
from phonemize import Phonemizer

class TextToSpeech:
    def __init__(self, model_path: str, config_path: str, phonikud_model: str):
        self.model = Piper(model_path, config_path)
        self.phonemizer = Phonemizer(phonikud_model)

    def create(self, text: str):
        phonemes = self.phonemizer.phonemize(text)
        return self.model.create(phonemes, is_phonemes=True)