import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

payload = {
    "text": "🚨 Revenue Alert\nRevenue pacing -6.3% vs target.\nSuggested action: Review pipeline conversion."
}

requests.post(SLACK_WEBHOOK, json=payload)
