import numpy as np
from record import Record
from vad import VAD
from noise_filter import NoiseFilter
from wake_word import WakeWord
from speech_to_text import SpeechToText
from agent_openai import OpenAIClient
from text_to_speech import TextToSpeech
from collections import deque
import time
import threading
import sounddevice as sd

class SpeechRecorder:
    def __init__(self):
        self.recorder = Record()
        self.vad = VAD()
        self.noise_filter = NoiseFilter()
        self.wake_word = WakeWord()
        self.stt = SpeechToText()
        self.openai = OpenAIClient()
        self.is_recording = False
        self.is_transcribing = False
        self.audio_buffer = deque(maxlen=3)  # ~0.1 seconds at 16kHz/512 samples
        self.recorded_audio = []
        self.tts = TextToSpeech('tts-model.onnx', 'tts-model.config.json', 'phonikud-1.0.int8.onnx')
        
    def transcribe_audio_segment(self, audio_segment):
        """Transcribe audio in a separate thread"""
        try:
            text = self.stt.transcribe(audio_segment)
            print(f"Transcribed: {text}")
            # Send to OpenAI and get response
            if text.strip():
                ai_response = self.openai.get_response(text)
                print(f"AI Response: {ai_response}")
                print("Creating TTS audio")
                samples, sample_rate = self.tts.create(ai_response)
                print("Playing TTS audio")
                sd.play(samples, sample_rate)
        except Exception as e:
            print(f"Transcription error: {e}")
        finally:
            self.is_transcribing = False
        
    def run(self):
        self.recorder.start()
        print(f"Recording sample rate: {self.recorder.sample_rate} Hz")
        wake_word_mode = True
        silence_count = 0
        
        try:
            while True:
                frame = self.recorder.read_frame()
                enhanced_frame = self.noise_filter.enhance(frame)
                
                if wake_word_mode and not self.is_transcribing:
                    self.audio_buffer.append(enhanced_frame)
                    if self.wake_word.detect(enhanced_frame):
                        wake_word_mode = False
                        self.is_recording = True
                        silence_count = 0
                        print("speech started")
                        # Include buffered audio from before wake word
                        self.recorded_audio = list(self.audio_buffer)
                elif self.is_recording:
                    self.recorded_audio.append(enhanced_frame)
                    if self.vad.is_speech(enhanced_frame):
                        silence_count = 0
                    else:
                        silence_count += 1
                        if silence_count > 30:
                            print("speech finished")
                            self.is_transcribing = True
                            
                            # Start transcription in separate thread
                            if self.recorded_audio:
                                audio_copy = self.recorded_audio.copy()
                                thread = threading.Thread(
                                    target=self.transcribe_audio_segment,
                                    args=(audio_copy,)
                                )
                                thread.start()
                            
                            # Reset state immediately
                            self.is_recording = False
                            silence_count = 0
                            wake_word_mode = True
                            self.recorded_audio = []
                            self.audio_buffer.clear()
                            
        except KeyboardInterrupt:
            pass
        finally:
            self.cleanup()
            
    def cleanup(self):
        self.recorder.stop()
        self.vad.cleanup()
        self.noise_filter.cleanup()
        self.wake_word.cleanup()

if __name__ == "__main__":
    recorder = SpeechRecorder()
    recorder.run()
