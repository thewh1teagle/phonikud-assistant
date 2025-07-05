import pvkoala

koala = pvkoala.create(access_key='${ACCESS_KEY}')

def get_next_audio_frame():
    pass

while True:
    enhanced_audio = koala.process(get_next_audio_frame())