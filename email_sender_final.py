import csv 
import json
from email.message import EmailMessage
import ssl
import smtplib
import requests 

# info of sender
email_sender = "detteerbareentesthackathon@gmail.com"
email_password = "jmaw ecnk yaxl kfjh"

# Example of body
subject = "Teste"
body = "DET FUNKAAAAAAAAA"

# Google Sheets CSV link 
csv_url = "https://docs.google.com/spreadsheets/d/1rcZpeuAnkxgmUH0SxpcSNsnBCiJ0vvuQ24HGs71YEx0/gviz/tq?tqx=out:csv"

# Function for getting the emails
def get_email_list():
    with open("email_database.json", "r") as file:  # Open JSON file
        data = json.load(file)  # Load JSON content
        return data.get("emails", [])  # Return the list of emails
    
# Get the email list
email_receivers = get_email_list()  

# Secure connection
context = ssl.create_default_context()

# Sending of emails to users
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    
    for email_receiver in email_receivers:
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        
        try:
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            print(f"Email sent to {email_receiver}")
            
        except smtplib.SMTPRecipientsRefused:
            print(f"Invalid email address: {email_receiver}")  # Print confirmaition