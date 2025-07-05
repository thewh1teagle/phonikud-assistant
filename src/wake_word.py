import pvporcupine
from config import PICOVOICE_TOKEN

class WakeWord:
    def __init__(self):
        self.porcupine = pvporcupine.create(
            access_key=PICOVOICE_TOKEN,
            # keyword_paths=['Yuval_en_mac_v3_0_0.ppn'],
            keywords=['picovoice', 'bumblebee']
        )
        
    def detect(self, audio_frame):
        keyword_index = self.porcupine.process(audio_frame)
        return keyword_index >= 0
        
    def cleanup(self):
        self.porcupine.delete()