import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def transcribe(self, audio_data):
        try:
            audio = sr.AudioData(audio_data.tobytes(), 16000, 2)
            text = self.recognizer.recognize_google(audio)
            return text
        except:
            return ""
