from email.message import EmailMessage
import ssl
import smtplib

#Basic info om hvem å sende fra og til + passordet til senderens email 
email_sender = "detteerbareentesthackathon@gmail.com"
email_password = "jmaw ecnk yaxl kfjh"
email_receiver = "chwarberg@gmail.com"

#Subjekt og selve "body" teksten, dette var bare en test
subjekt = "Teste"
body = "DET FUNKAAAAAAAAA"

#Hva å inkludere i emailen
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subjekt
em.set_content(body)

#Lager en sikker forbinnelse mellom partene
context = ssl.create_default_context()

#Sendingen av emailen over smtp ved hjelp av ssl
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password,)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
