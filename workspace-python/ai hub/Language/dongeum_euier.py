#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/Homonym"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
word = "말"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "word": word
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode]" + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                      