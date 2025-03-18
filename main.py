import json
import news_api

# Test for the rss module
api = news_api.RSS()
api.articles[0].print_article()
