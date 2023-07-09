import requests

url = 'http://localhost:5000/v1/get-logs'
data = {
    'source': 'web',
    'level': 'error'
}

response = requests.post(url, json=data)
logs = response.json()

print(logs)
