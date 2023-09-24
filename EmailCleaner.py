import re

def clean_email(email):
    # Remove special characters
    cleaned_email = re.sub('[^a-zA-Z0-9]', ' ', email)
    
    # Remove extra white spaces
    cleaned_email = re.sub('\s+', ' ', cleaned_email)
    
    # Convert to lowercase
    cleaned_email = cleaned_email.lower()
    
    return cleaned_email
