import requests

url = 'http://localhost:8801/login'

data = {
    "first_name": 'Elisee',
    "last_name": 'Azouma'
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to connect to the API. Status code: {response.status_code}")
