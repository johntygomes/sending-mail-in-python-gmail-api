from flask import Flask
################################################################
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
################################################################

app = Flask(__name__)

@app.route("/")
def index():
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    emailMsg = 'You won The Match'
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = 'natgomes7@gmail.com'
    mimeMessage['subject'] = 'You won'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    # print(message)
    return "Hello World!"
