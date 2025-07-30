## 🔐 Gmail API Setup (Optional)

This app supports Gmail inbox scanning via OAuth2.

### Steps:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **Gmail API**
3. Create **OAuth 2.0 Client ID** (Application type: Desktop)
4. Download `credentials.json` and place in project root
5. On first run, you'll be prompted to log in and grant access
6. Token will be saved to `token.pickle` (already in .gitignore)

> ⚠️ Never commit `credentials.json` or `token.pickle` to GitHub!