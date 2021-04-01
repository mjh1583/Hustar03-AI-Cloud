#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WikiQA"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
question = "싸이가 누구야?"
# 질문 응답 엔진의 종류 로서 UTF-8 인코딩된 텍스트만 지원
# irqa: 언어분석 기반과 기계독해 기반의 질의응답을 통합한 질의응답 방식
# kbqa: 지식베이스 기반의 질의응답 방식
# hybridqa: irqa와 kbqa를 통합한 질의응답 방식
type = "hybridqa"
 
requestJson = {
"access_key": accessKey,
"argument": {
    "question": question,
    "type": type
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