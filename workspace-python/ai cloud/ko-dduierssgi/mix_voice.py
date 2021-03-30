import requests

post_url = 'http://svc.saltlux.ai:31781'

headers = {
    'Content-Type': 'application/json'
}

json_data = {
    "key": "4b8f26bb-e2ca-42b5-8732-1c343dfb388b",
    "serviceId": "01844762252",
    "argument": {
        "voice": "test",
        "text": "마! 니 광안리 등킨드나쓰 무봤나?",
        "cache": "False",
        "replace": "False",
        "type": "wav"
    }
}

response = requests.post(
    post_url,
    headers = headers, 
    json = json_data
)

print(response.status_code)
print(response.text)