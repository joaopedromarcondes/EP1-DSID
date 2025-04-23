# json-client.py
import requests
import json

url = "http://localhost:5000"

payload = {
    "jsonrpc": "2.0",
    "method": "soma",
    "params": {"a": 1, "b": 2},
    "id": 1
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Resultado:", response.json()["result"])
