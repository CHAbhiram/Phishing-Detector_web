## 🛡️ PhishingGuard: AI-Powered Email Security Web App

> **Detect, Analyze, and Protect Against Phishing Emails**

---

### 📝 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Screenshots](#screenshots)
4. [Installation & Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Dependencies](#dependencies)
---

## ✨ Overview

**PhishingGuard** is a web-based tool designed to detect phishing emails using both **machine learning (ML)** and heuristic analysis. It allows users to:
- Upload `.eml` email files for analysis.
- Scan their Gmail inbox for suspicious emails.
- Get real-time feedback on whether an email is **phishing** or **safe**.

This project is ideal for:
- **Individuals**: Protect personal accounts.
- **Teams**: Train employees on phishing detection.
- **Educators**: Demonstrate cybersecurity concepts.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| **AI Detection** | Uses ML to classify emails as phishing or safe. |
| **Heuristic Analysis** | Flags suspicious keywords, links, and domains. |
| **Gmail Integration** | Scans your inbox for potential threats. |
| **User-Friendly UI** | Clean, responsive design for easy use. |
| **Secure** | No sensitive data stored; uses local analysis. |

---

## 🖼️ Screenshots

### 1. **Analysis Results**
<img width="1880" height="965" alt="Screenshot 2025-07-30 130517" src="https://github.com/user-attachments/assets/d8a22210-5ba5-45ae-9f37-649a3e2b38df" />

- **File Preview**: Displays part of the email content.
- **AI Verdict**: Shows whether the email is phishing or safe.
- **Confidence Score**: Indicates model certainty.
- **Scan Another**: Option to upload another email.

### 2. **Upload & Scan Interface**
<img width="1877" height="970" alt="Screenshot 2025-07-30 130528" src="https://github.com/user-attachments/assets/4dd7b3a3-0559-4099-b22e-4d0dcdc44f92" />

- **Email Upload**: Drag-and-drop or select `.eml` files.
- **Gmail Integration**: Scan entire inbox with OAuth2.
- **Responsive Design**: Works on desktop and mobile.

---

## 🔧 Installation and Setup

### Prerequisites
- **Python 3.9+**: Ensure you have Python installed.
- **Virtual Environment**: Recommended for dependency isolation.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/phishingguard-web.git
   cd phishingguard-web
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```
   - The app will start on `http://127.0.0.1:5000`.

5. **Optional: Gmail Integration**
   - Go to [Google Cloud Console](https://console.cloud.google.com/) → Create a project → Enable **Gmail API**.
   - Download `credentials.json` and place it in the root directory.
   - First run will prompt you to authenticate via browser.

## 🔐 Gmail API Setup (Optional)

This app supports Gmail inbox scanning via OAuth2.

### Steps:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **Gmail API**
3. Create **OAuth 2.0 Client ID** (Application type: Desktop)
4. Download `credentials.json` and place in project root
5. On first run, you'll be prompted to log in and grant access
6. Token will be saved to `token.pickle` (already in .gitignore)

---

## 🏃‍♂️ Usage

1. **Upload an `.eml` File**
   - Navigate to `/results` after uploading.
   - View AI verdict, confidence score, and file preview.

2. **Scan Gmail Inbox**
   - Click "Scan Gmail Inbox."
   - Authenticate with Google OAuth2.
   - Review recent emails flagged as suspicious.

3. **Interpret Results**
   - **Red Alert**: High-risk email detected.
   - **Green Check**: Safe email confirmed.
   - **Neutral**: Heuristic analysis pending.

---

## ⚙️ Dependencies

The project relies on the following libraries:

| Library | Purpose |
|---------|---------|
| **Flask** | Web framework |
| **scikit-learn** | Machine learning |
| **pandas** | Data processing |
| **google-api-python-client** | Gmail API integration |
| **joblib** | Model persistence |
| **tldextract** | Domain parsing |
| **requests** | HTTP requests |
| **Werkzeug** | Flask utilities |

---

## 🤝 Contributing

Feel free to open issues or pull requests if you'd like to:
- Improve accuracy
- Add new features
- Fix bugs

---

## 🌟 Acknowledgments

- **Dataset**: Synthetic phishing emails created for educational purposes.
- **Inspiration**: Real-world phishing attacks analyzed by security researchers.

---

### 🎁 Sample Output

Here’s what you’ll see when analyzing a phishing email:

```plaintext
File: email_1.eml
Preview: Never agree to be a loser Buck up, your troubles caused by small dimension will soon be over! Become a lover no woman will be able to resist! http://whitedone.com/ come. Even as Nazi tanks were roll...
AI Verdict: 🚨 PHISHING
Confidence: 0.5 (ML)
```

---

### 🚨 Disclaimer

This tool is for **educational and defensive purposes only**. Do not use it to:
- Attack systems you don't own.
- Scan emails without permission.
- Harass or violate privacy.

The author is not responsible for misuse.

---

## 🚀 How to Contribute

1. **Fork the Repository**
2. **Clone Locally**
   ```bash
   git clone https://github.com/yourusername/phishingguard-web.git
   ```
3. **Make Changes**
4. **Commit & Push**
   ```bash
   git add .
   git commit -m "Add feature: XYZ"
   git push origin main
   ```
5. **Open a Pull Request**

---

## 🌐 Deployment

You can deploy this app to platforms like:
- **Render**
- **Heroku**
- **AWS Elastic Beanstalk**
- **Docker + Docker Hub**

---

## 📦 Files Structure

```
phishingguard-web/
├── app.py                          # Flask main app
├── detector/
│   ├── core.py                     # Detection logic
│   ├── ml_model.pkl                # Trained ML model
│   └── vectorizer.pkl             # TF-IDF vectorizer
├── templates/
│   ├── index.html                  # Upload & scan
│   ├── results.html
│   └── inbox.html                 # Gmail integration
├── static/
│   └── style.css
├── models/                         # Training scripts
│   └── train_ml_model.py
├── gmail_auth.py                   # OAuth2 for Gmail
├── requirements.txt
├── sample_emails/                  # Test files
└── README.md
```

---

## 🎉 Conclusion

**PhishingGuard** empowers users to protect themselves against phishing attacks. Whether you're an individual, team, or educator, this tool provides a practical way to analyze and secure your emails.

---

### 📸 Screenshot Folder (`screenshots/`)

Ensure you have a folder named `screenshots/` in your repository root and upload the two images there. Then update the `README.md` with the correct paths:

```markdown
### 1. **Analysis Results**
![Analysis Results](./screenshots/analysis_results.png)

### 2. **Upload & Scan Interface**
![Upload & Scan](./screenshots/upload_scan.png)
```

---
