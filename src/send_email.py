import smtplib
from email.message import EmailMessage
import os
import sys

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

print("DEBUG: Script started")

if not EMAIL_USER or not EMAIL_PASS:
    print("ERROR: Missing EMAIL_USER or EMAIL_PASS")
    sys.exit(1)

print("DEBUG: Credentials found")

msg = EmailMessage()
msg.set_content("""
🚨 Revenue Alert

Revenue pacing is below target.
Suggested action: Review pipeline conversion.
""")

msg["Subject"] = "Revenue Alert – Automated Analytics"
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_USER

try:
    print("DEBUG: Connecting to SMTP server...")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        print("DEBUG: Logging in...")
        server.login(EMAIL_USER, EMAIL_PASS)
        print("DEBUG: Sending email...")
        server.send_message(msg)

    print("SUCCESS: Email sent")

except Exception as e:
    print("ERROR: Email failed")
    print(str(e))
    raise

