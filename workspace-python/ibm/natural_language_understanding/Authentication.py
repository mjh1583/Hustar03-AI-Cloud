import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, EmotionOptions, KeywordsOptions, EntitiesOptions

authenticator = IAMAuthenticator('CUzLG-rDruMnsWUY2CBidLaonQbsoCp-qcebL-ym64ZC')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

# 자연어 이해
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/d9dfb8fa-6d82-48d4-a5b2-8bb8d4300fad')

# 카테고리 범주 반환
# response = natural_language_understanding.analyze(
#     url='www.ibm.com',
#     features=Features(categories=CategoriesOptions(limit=3))).get_result()

# print(json.dumps(response, indent=2))


# 감정 분석
# response = natural_language_understanding.analyze(
#     html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
#     features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

# print(json.dumps(response, indent=2))

# 텍스트 분석
response = natural_language_understanding.analyze(
    url='https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#analyze',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=2))).get_result()

print(json.dumps(response, indent=2))

