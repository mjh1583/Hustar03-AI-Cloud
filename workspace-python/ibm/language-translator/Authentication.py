import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('cDOABBhdRM6n3tc_r152BmdoFnbZpGGfO08RrawVrVq8')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/25e965b6-f4e4-4cd2-b75c-50288305cf75')

# 지원되는 언어 나열
# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

# 번역
# translation = language_translator.translate(
#     text='Hello, how are you today?',
#     model_id='en-ko').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))

# 식별 가능한 언어 나열 (어떤 나라의 언어인지 판별)
# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))

# 판별
# language = language_translator.identify(
#     '한국어 konglish english').get_result()
# print(json.dumps(language, indent=2))

# 문서 번역
# with open('test.pptx', 'rb') as file:
#     result = language_translator.translate_document(
#         file=file,
#         file_content_type='application/mspowerpoint',
#         filename='test2.pdf',
#         model_id='en-ko').get_result()
#     print(json.dumps(result, indent=2))
    
# 번역된 문서 받기 (번역한 문서의 아이디 값을 가져와서 넣어주고 문서의 확장자가 같아야 함)
with open('translated.pptx', 'wb') as f:
    result = language_translator.get_translated_document(
        document_id='3a6f0121-04f8-46f0-bb9a-a91f2b5cf0ba',
        accept='application/mspowerpoint').get_result()
    f.write(result.content)