import numpy as np
from pywhispercpp.model import Model
from huggingface_hub import hf_hub_download

class SpeechToText:
    def __init__(self, model_path):
        self.model = Model(model_path)
        
    def transcribe(self, audio_data):
        try:
            # Convert audio data to proper format
            audio_array = np.concatenate(audio_data)
            
            # Convert to float32 and normalize if needed
            if audio_array.dtype == np.int16:
                audio_array = audio_array.astype(np.float32) / 32768.0
            
            # Try to transcribe directly with ndarray
            segs = self.model.transcribe(audio_array, language='he')
            text = ' '.join(segment.text for segment in segs)
            return text
        except Exception as e:
            return ""
