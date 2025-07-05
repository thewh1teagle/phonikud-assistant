import pvcobra
from config import PICOVOICE_TOKEN

class VAD:
    def __init__(self):
        self.cobra = pvcobra.create(access_key=PICOVOICE_TOKEN)
        
    def is_speech(self, audio_frame):
        voice_probability = self.cobra.process(audio_frame)
        return voice_probability > 0.5
        
    def cleanup(self):
        self.cobra.delete()