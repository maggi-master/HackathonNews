import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

news = news_api.FetchNews()
tags = news_api.Tags(["Internasjonal politikk", "Norge", "Russland", "Ukraina", "Europa"])

articles = news.search(tags)
print(f"Fant {len(articles)} relvante artikler av totalt {len(news)} artikler basert på disse temane {tags}")

for article in articles[:3]:
    print(article)