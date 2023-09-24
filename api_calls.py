import requests


def send_request(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
