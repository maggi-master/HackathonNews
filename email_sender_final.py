import json
import smtplib
import ssl
from email.message import EmailMessage
import requests

class EmailSender:
    def __init__(self, email_sender, email_password, json_url):
        """Initialize email sender details and JSON file source"""
        self.email_sender = email_sender
        self.email_password = email_password
        self.json_url = json_url
        self.email_receivers = self.fetch_emails()

    def fetch_emails(self):
        """Fetch emails from the JSON file in the website"""
        try:
            response = requests.get(self.json_url)
            response.raise_for_status()
            data = response.json()
            return data.get("emails", [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching emails: {e}")
            return []

    def send_emails(self, subject, body):
        """Send emails to all recipients"""
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            
            for email_receiver in self.email_receivers:
                try:
                    em = EmailMessage()
                    em["From"] = self.email_sender
                    em["To"] = email_receiver
                    em["Subject"] = subject
                    em.set_content(body)
                    
                    smtp.sendmail(self.email_sender, email_receiver, em.as_string())
                    print(f"Email sent to {email_receiver}")
                except Exception as e:
                    print(f"Failed to send to {email_receiver}: {e}")

# Usage Example
if __name__ == "__main__":
    EMAIL_SENDER = "detteerbareentesthackathon@gmail.com"
    EMAIL_PASSWORD = "jmaw ecnk yaxl kfjh"  
    JSON_URL = ""

    email_sender = EmailSender(EMAIL_SENDER, EMAIL_PASSWORD, JSON_URL)
    email_sender.send_emails("Test Subject", "This is a test email.")