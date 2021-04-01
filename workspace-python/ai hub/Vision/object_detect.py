#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
imageFilePath = "object_detect_person.jpg"
imageFilePath = "object_detect_airplane.jpg"
imageFilePath = "object_detect_boat.jpg"
imageFilePath = "object_detect_cat.jpg"
imageFilePath = "2321589517.jpg"
imageFilePath = "111012145.jpg"
type = "jpg"
 
file = open(imageFilePath, "rb")
imageContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "type": type,
        "file": imageContents
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
print(response.data)