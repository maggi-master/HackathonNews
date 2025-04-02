import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

news = news_api.FetchNews()
tags = news_api.Tags(["internasjonal politikk", "norge", "russland", "Ukraina", "Europa"])

articles = news.search(tags)
print(f"Fant {len(articles)} relvante artikler av totalt {len(news)} artikler basert på disse temane {tags}")