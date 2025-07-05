import phonikud
from phonikud_onnx import Phonikud

class Phonemizer:
    def __init__(self, model_path: str):
        self.model = Phonikud(model_path)
    
    def phonemize(self, text: str) -> str:
        vocalized = self.model.add_diacritics(text)
        phonemes = phonikud.phonemize(vocalized)
        return phonemes