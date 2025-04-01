import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

api = news_api.Articles()
tags = news_api.Tags(["internasjonal politikk", "norge", "russland"])

for article in api.search(tags):
    print(article)