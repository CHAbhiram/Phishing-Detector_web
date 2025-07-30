# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from detector import core
from gmail_auth import authenticate_gmail, get_recent_emails

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if 'email_file' not in request.files:
        flash('No file uploaded')
        return redirect(url_for('index'))
    
    file = request.files['email_file']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    try:
        result = core.analyze_email(filepath)
        return render_template('results.html', result=result)
    except Exception as e:
        flash(f'Error analyzing email: {str(e)}')
        return redirect(url_for('index'))

@app.route('/inbox')
def inbox():
    try:
        service = authenticate_gmail()
        emails = get_recent_emails(service, 10)
        return render_template('inbox.html', emails=emails)
    except Exception as e:
        flash(f'Gmail error: {str(e)}. Have you set up credentials.json?')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)