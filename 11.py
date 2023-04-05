import requests
import json

print('http://127.0.0.1:5000/random_json')
resp = requests.get('http://127.0.0.1:5000/random_json')
print(resp)
print(resp.status_code)
print(resp.request.body)
print(resp._content)
print(resp._content.decode())
print(json.loads(resp._content.decode()))

print('http://127.0.0.1:5000/random_json_str')
resp = requests.get('http://127.0.0.1:5000/random_json_str')
print(resp)
print(resp.status_code)
print(resp.request.body)
print(resp._content)
print(resp._content.decode())
print(json.loads(resp._content.decode()))