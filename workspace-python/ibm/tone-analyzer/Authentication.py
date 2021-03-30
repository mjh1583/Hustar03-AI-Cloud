import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('T7b6yapBD5VglqZs7hNz_imRbFcv7nHGTaP5A8jBwFPj')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.kr-seo.tone-analyzer.watson.cloud.ibm.com/instances/82734502-e1cb-4afc-8e73-4588e21b84bb')

text = 'Team, I know that times are tough! Product '\
    'sales have been disappointing for the past three '\
    'quarters. We have a competitive product, but we '\
    'need to do a better job of selling it!'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))