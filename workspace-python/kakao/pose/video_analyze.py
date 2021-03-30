import os
import requests

APP_KEY = '6bd8276ee95a465348f851c8992fc437'
VIDEO_URL = 'http://example.com/example.mp4'
# VIDEO_FILE_PATH = 'example.mp4'

session = requests.Session()
session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})

# URL로 영상 입력시
response = session.post('https://cv-api.kakaobrain.com/pose/job', data={'video_url': VIDEO_URL})
print(response.status_code, response.json())
job_id = response.json()['job_id']

# 파일로 영상 입력시
# assert os.path.getsize(VIDEO_FILE_PATH) < 5e7
# with open(VIDEO_FILE_PATH, 'rb') as f:
#     response = session.post('https://cv-api.kakaobrain.com/pose/job', files=[('file', f)])
#     print(response.status_code, response.json())
#     job_id = response.json()['job_id']