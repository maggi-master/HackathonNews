import news_api
from database import ServerFirebaseConfig, FirebaseHandler
from dotenv import load_dotenv
import os
import smtplib
import ssl
import markdown
from email.mime.text import MIMEText
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
        email = analyzer.generate_email()

        f = open(f"./emails/{user["email"]}.md", "w")
        f.write(email)
        f.close()

        smtp.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_PASSWORD"))
        html = markdown.markdown(email)
        msg = MIMEText(html, 'html')
        msg["From"] = os.getenv("EMAIL_SENDER")
        msg["To"] = user["email"]
        msg["Subject"] = "Dagens Nyheter"
        
        smtp.sendmail(os.getenv("EMAIL_SENDER"), user["email"], msg.as_string())
        print(f"Email Sendt to {user["email"]}")