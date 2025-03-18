import feedparser as fp
from .rss_feeds import RSS_FEEDS
from .Article import Article

class RSS:
    def __init__(self) -> None:
        self.articles = []
        self.parse_feeds()

    def parse_feed(self, source_name:str, feed:str) -> None:
        """Parses single feed and appends to articles list"""
        parsed_feed = fp.parse(feed)
        for entry in parsed_feed.entries:
            article = Article(entry)
            article.update({"source": source_name})
            self.articles.append(article)
    
    def parse_feeds(self) -> None:
        """Parses alle the feeds from RSS_FEEDS variable using the parse_feed function"""
        for source_name, feed in RSS_FEEDS.items():
            self.parse_feed(source_name, feed)