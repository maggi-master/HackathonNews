import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

api = news_api.Articles()
articles = api.get_articles()
articles[0].update_content()
print(articles[0])