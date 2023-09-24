import re

def parse_email(email):
    # Extract subject
    subject = re.search('Subject: (.+)', email)
    if subject:
        subject = subject.group(1)
    
    # Extract sender
    sender = re.search('From: (.+)', email)
    if sender:
        sender = sender.group(1)
    
    # Extract body
    body = re.search('Body: (.+)', email)
    if body:
        body = body.group(1)
    
    return {
        'subject': subject,
        'sender': sender,
        'body': body
    }
