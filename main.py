import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

news = news_api.FetchNews()
tags = news_api.Tags(["Internasjonal politikk", "Russland", "Ukraina", "Europa"])

articles = news.search(tags)
print(f"Fant {len(articles)} relvante artikler av totalt {len(news)} artikler basert på disse temane {tags}")

analyzer = news_api.ArticleCollection(articles)
email = analyzer.generate_email()

with open("output.txt", "w") as file:
    file.write(email)

print(email)