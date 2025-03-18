import json
import news_api

api = news_api.rss()
print(json.dumps(api.articles[0], sort_keys=True, indent=4))
