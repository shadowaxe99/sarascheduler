import requests

def send_message(message):
    url = 'https://api.emberbot.dev/send'
    headers = {'Content-Type': 'application/json'}
    data = {
        'message': message
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print('Message sent successfully')
    else:
        print('Failed to send message')
