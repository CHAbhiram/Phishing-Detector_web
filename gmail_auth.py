# gmail_auth.py
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle
import os

# Scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_recent_emails(service, max_results=10):
    results = service.users().messages().list(
        userId='me', maxResults=max_results, labelIds=['INBOX']
    ).execute()
    
    messages = results.get('messages', [])
    emails = []
    
    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me', id=msg['id']
        ).execute()
        
        headers = msg_data['payload']['headers']
        subject = [h['value'] for h in headers if h['name'] == 'Subject']
        sender = [h['value'] for h in headers if h['name'] == 'From']
        
        emails.append({
            'id': msg['id'],
            'subject': subject[0] if subject else 'No Subject',
            'from': sender[0] if sender else 'Unknown',
            'snippet': msg_data.get('snippet', '')[:100]
        })
    
    return emails