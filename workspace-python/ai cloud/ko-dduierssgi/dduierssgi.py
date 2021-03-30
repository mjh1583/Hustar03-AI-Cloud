import requests

post_url = 'http://svc.saltlux.ai:31781'

headers = {
    'Content-Type': 'application/json'
}

json_data = {
    "key": "4b8f26bb-e2ca-42b5-8732-1c343dfb388b",
    "serviceId": "01139773605",
    "argument": {
        "question": "아버지가방에들어가셨습니다."
    }
}

response = requests.post(
    post_url,
    headers = headers, 
    json = json_data
)

print(response.status_code)
print(response.text)