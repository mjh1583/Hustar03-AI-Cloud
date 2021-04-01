#-*- coding:utf-8 -*-
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/HumanParsing"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"

imageFilePath = "person_detect_1.jpg"
imageFilePath = "person_detect_2.jpg"
imageFilePath = "person_detect_3.jpg"
imageFilePath = "person_detect_4.jpg"
imageFilePath = "person_detect_4.jpg"
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