import news_api
import logging as log

# Test for the rss module
log.basicConfig(level=log.ERROR)

api = news_api.RSS()
articles = api.get_articles()
print(articles[3].update_content())
articles[3].print_article()