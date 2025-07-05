import pvkoala
from config import PICOVOICE_TOKEN

class NoiseFilter:
    def __init__(self):
        self.koala = pvkoala.create(access_key=PICOVOICE_TOKEN)
        
    def enhance(self, audio_frame):
        enhanced = []
        for i in range(0, len(audio_frame), 256):
            chunk = audio_frame[i:i+256]
            if len(chunk) == 256:
                enhanced.extend(self.koala.process(chunk))
        return enhanced[:len(audio_frame)]
        
    def cleanup(self):
        self.koala.delete()