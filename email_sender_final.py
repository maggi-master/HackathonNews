import csv 
from email.message import EmailMessage
import ssl
import smtplib
import requests 

# Basic info om sender osv
email_sender = "detteerbareentesthackathon@gmail.com"
email_password = "jmaw ecnk yaxl kfjh"

# Eksempel på subjekt og body
subject = "Teste"
body = "DET FUNKAAAAAAAAA"

# Google Sheets CSV link (replace with your actual link)
csv_url = "https://docs.google.com/spreadsheets/d/1rcZpeuAnkxgmUH0SxpcSNsnBCiJ0vvuQ24HGs71YEx0/gviz/tq?tqx=out:csv"

# Function to get emails from Google Sheets
def get_email_list():
    response = requests.get(csv_url)  # csv_url is already in scope, no need to pass it
    response.raise_for_status()  # Ensure we got the file
    
    emails = []
    reader = csv.reader(response.text.splitlines())  # Read CSV content
    for row in reader:
        if row:
            emails.append(row[0])  # Assume emails are in the first column
    return emails

# Få listen på emailene
email_receivers = get_email_list()  # Now no argument needed

# Sikker forbinnelse laget
context = ssl.create_default_context()

# Sendingen av emailene til brukerene
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    
    for email_receiver in email_receivers:
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = email_receiver
        em["Subject"] = subject
        em.set_content(body)
        
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"Email sent to {email_receiver}")  # Print bekreftelse