# detector/core.py
import os
import re
import email
from email import policy
import tldextract
import joblib

# Load ML model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model.pkl')
model = joblib.load(MODEL_PATH)

SUSPICIOUS_KEYWORDS = ['urgent', 'verify', 'suspended', 'click', 'login', 'immediate']

def extract_text_from_email(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        msg = email.message_from_file(f, policy=policy.default)
    
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                payload = part.get_payload(decode=True)
                if payload:
                    try:
                        body += payload.decode('utf-8', errors='ignore')
                    except:
                        body += payload.decode('latin1')
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            try:
                body = payload.decode('utf-8', errors='ignore')
            except:
                body = payload.decode('latin1')
    
    return msg.get('Subject', '') + " " + body

def analyze_email(file_path):
    text = extract_text_from_email(file_path)
    
    # ML Prediction
    pred = model.predict([text])[0]
    prob = model.predict_proba([text])[0]
    ml_score = max(prob)  # confidence
    
    # Heuristic analysis
    lines = text.lower().split()
    keyword_matches = [w for w in SUSPICIOUS_KEYWORDS if w in text.lower()]
    
    result = {
        'filename': os.path.basename(file_path),
        'text_preview': text[:200] + "...",
        'ml_prediction': pred,
        'ml_confidence': round(ml_score, 3),
        'heuristic_warnings': keyword_matches,
        'total_risk_score': (ml_score * 0.7) + (len(keyword_matches) * 0.05),
        'is_phishing': pred == 'phishing' or len(keyword_matches) > 2
    }
    return result