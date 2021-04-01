
#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation" # 영어
# openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor" # 한국어
 
# 발음평가의 입력 음성 언어 코드입니다. 요청할 수 있는 언어 코드는 아래와 같습니다.
# english: 영어 발음평가 코드
# korean: 한국어 발음평가 코드
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
audioFilePath = "PRO_F_D01S03_01S.pcm"
audioFilePath = "PRO_M_20csg0029.pcm"
languageCode = "english"
script = "PRONUNCIATION_SCRIPT"
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "script": script,
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                      