import requests
import json

payload = {'send': 'data'}
headers = {'content-type': 'application/json'}

response = requests.post('http://127.0.0.1:3000/', data=json.dumps(payload), headers=headers)

print(response.json())
