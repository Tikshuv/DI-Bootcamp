import requests


slack_webhook_url = "https://hooks.slack.com/services/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"


def send_slack_notification(message):
    payload = {"text": message}
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}, {response.text}")


send_slack_notification("Hello from your API!")
