import json
import news_api

# Test for the rss module
api = news_api.rss()
print(json.dumps(api.articles[0], sort_keys=True, indent=4))
