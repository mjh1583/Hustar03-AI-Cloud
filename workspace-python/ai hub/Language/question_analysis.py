#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseQAnal"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
text = "헝가리의 수도는?"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text
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