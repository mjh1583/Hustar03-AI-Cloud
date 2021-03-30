import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Mfg7_1Xw02agbAbcDxpqkcQcOltjlkUEFnm9Wjq05giV')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.kr-seo.text-to-speech.watson.cloud.ibm.com/instances/fcaec740-dbdc-4754-ac16-9cea969640e8')

# 목소리 리스트 나열
voices = text_to_speech.list_voices().get_result()
print(json.dumps(voices, indent=2))

# 목소리 합성 : 지정된 문자열을 소리 파일로 변환함
with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'moo yha hou',
            voice='en-US_LisaVoice',
            accept='audio/wav'        
        ).get_result().content)

# 지정된 단어의 발음을 가져옴
pronunciation = text_to_speech.get_pronunciation(
    text='Holy',
    voice='en-US_AllisonV3Voice',
    format='ibm'
).get_result()
print(json.dumps(pronunciation, indent=2))

