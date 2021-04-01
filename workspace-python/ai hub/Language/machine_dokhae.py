#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/MRCServlet"
accessKey = "d256e77e-d1e5-44af-ad88-0895b6428e6f"
question = "헝가리의 수도가 어디야?"
passage = "헝가리국(헝가리어: Magyarország 머저로르사그[*] [ˈmɒɟɒrorsaːɡ] 이 소리의 정보듣기 (도움말·정보)), 약칭 헝가리(헝가리어: Magyar 머저르[*], 영어: Hungary 헝가리[*], 문화어: 웽그리아, 마쟈르)는 중앙유럽에 있는 내륙국이며 수도는 부다페스트이다. 면적은 대한민국의 약 10분의 9이고, 전체 인구는 서울특별시의 인구와 유사하다."
 
requestJson = {
"access_key": accessKey,
    "argument": {
        "question": question,
        "passage": passage
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