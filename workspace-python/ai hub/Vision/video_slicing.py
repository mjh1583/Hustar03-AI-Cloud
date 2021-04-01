#-*- coding:utf-8 -*-
import urllib3
import json
import os

openApiURL = "http://aiopen.etri.re.kr:8000/VideoParse"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"

videoFilePath  = "demo-1.mp4"
videoFilePath  = "demo-2.mp4"
videoFilePath  = "demo-3.mp4"
videoFilePath  = "demo-3.mp4"

file = open(videoFilePath,'rb')
fileContent = file.read()
file.close();

requestJson = {
	"access_key": accessKey,
	"argument": {}
}

http = urllib3.PoolManager()
response = http.request(
	"POST",
	openApiURL,
	fields={
		'json': json.dumps(requestJson),
		'uploadfile': (os.path.basename(file.name), fileContent)
	}
)

print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data)
			