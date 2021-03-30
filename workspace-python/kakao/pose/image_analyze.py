import requests
APP_KEY = '6bd8276ee95a465348f851c8992fc437'
IMAGE_URL = 'https://blog.kakaocdn.net/dn/er1OsA/btqEo6Jjqi1/4yBKY4ZvF95GnUwgcPEWpK/img.jpg'
IMAGE_FILE_PATH = 'D:\workspace-python\kakao\pose\images\pose_image.jpg'
session = requests.Session()
session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})

# URL로 이미지 입력시
response = session.post('https://cv-api.kakaobrain.com/pose', data={'image_url': IMAGE_URL})
print(response.status_code, response.json())

# 파일로 이미지 입력시
with open(IMAGE_FILE_PATH, 'rb') as f:
    response = session.post('https://cv-api.kakaobrain.com/pose', files=[('file', f)])
    print(response.status_code, response.json())