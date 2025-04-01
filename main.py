import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

api = news_api.Articles()
api.embedd_articles()
articles = api.get_articles()
print(articles[0].vector.shape[0])
articles[0].update_content()
print(articles[0])