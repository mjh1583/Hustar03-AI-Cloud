#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/WordRel"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
firstWord = '사과'
secondWord = '배'
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        'first_word': firstWord,
        'second_word': secondWord,
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