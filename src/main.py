import numpy as np
from record import Record
from vad import VAD
from noise_filter import NoiseFilter
import time

class SpeechRecorder:
    def __init__(self):
        self.recorder = Record()
        self.vad = VAD()
        self.noise_filter = NoiseFilter()
        self.is_recording = False
        
    def run(self):
        self.recorder.start()
        speech_detected = False
        silence_count = 0
        
        try:
            while True:
                frame = self.recorder.read_frame()
                enhanced_frame = self.noise_filter.enhance(frame)
                
                if self.vad.is_speech(enhanced_frame):
                    if not speech_detected:
                        speech_detected = True
                        self.is_recording = True
                        print("speech started")
                    silence_count = 0
                else:
                    if speech_detected:
                        silence_count += 1
                        if silence_count > 30:
                            print("speech finished")
                            speech_detected = False
                            self.is_recording = False
                            silence_count = 0
                            
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()
            
    def cleanup(self):
        self.recorder.stop()
        self.vad.cleanup()
        self.noise_filter.cleanup()

if __name__ == "__main__":
    recorder = SpeechRecorder()
    recorder.run()
