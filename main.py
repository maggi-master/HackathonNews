import news_api
from database import ServerFirebaseConfig, FirebaseHandler
import smtplib
from dotenv import load_dotenv
import os
import smtplib
import ssl
from email.message import EmailMessage
load_dotenv()

config = ServerFirebaseConfig()
database = FirebaseHandler(config)
user_data = database.get_all_users() #list[dict]
news = news_api.FetchNews()
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    for user in user_data:
        if len(user["tags"])==0:
            continue
        tags = news_api.Tags(user["tags"])
        tags.embedd_tags()
        articles = news.search(tags, 0.37)
        if len(articles)==0:
            continue
        print(f"Fant {len(articles)} relvante artikler av totalt {len(news)} artikler basert på disse temane {tags}")

        analyzer = news_api.ArticleCollection(articles, tags)
        BODY = analyzer.generate_email()
        print(BODY)
        
        TO_EMAIL = user["email"]
        SUBJECT = "Dagens Nyheter"
        EMAIL_SENDER = os.getenv("EMAIL_SENDER")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        em = EmailMessage()
        em["From"] = EMAIL_SENDER
        em["To"] = TO_EMAIL
        em["Subject"] = SUBJECT
        em.set_content(BODY)
        
        smtp.sendmail(EMAIL_SENDER, TO_EMAIL, em.as_string())
        print(f"Email Sendt to {TO_EMAIL}")