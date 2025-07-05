import pvcobra

cobra = pvcobra.create(access_key='${ACCESS_KEY}')


def get_next_audio_frame():
    pass

while True:
    audio_frame = get_next_audio_frame()
    voice_probability = cobra.process(audio_frame)