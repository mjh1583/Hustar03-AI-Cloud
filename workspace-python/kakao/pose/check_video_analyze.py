import requests
APP_KEY = '6bd8276ee95a465348f851c8992fc437'
session = requests.Session()
session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})
response = session.get('https://cv-api.kakaobrain.com/pose/job/' + '93ec5d51-c1de-4a25-97af-e784418a66aa')
print(response.status_code, response.json())