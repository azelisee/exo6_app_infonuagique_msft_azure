import requests

#url = 'http://localhost:8801/login'
#url ='https://rcwlogin.azurewebsites.net/login'
url = 'http://localhost:8802/prod'

data = {
    "num1": 45,
    "num2": 15,
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to connect to the API. Status code: {response.status_code}")
