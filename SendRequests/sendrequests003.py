import json
import requests

# 请求体body
payload_tuples = [('key1', 'value55555'), ('key2', 'value4444444')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)

payload_dict = {'key3': ['value7777', 'value88888']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)

json.dumps(r1.json(), indent=2, ensure_ascii=False)
