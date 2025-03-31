import feedparser as fp
from .rss_feeds import RSS_FEEDS
from .Article import Article

class Articles:
    def __init__(self) -> None:
        self._articles = []
        self._parse_feeds()

    def _parse_feed(self, source_name:str, feed:str) -> None:
        """Parses single feed and appends to articles list"""
        parsed_feed = fp.parse(feed)
        for entry in parsed_feed.entries:
            article = Article(entry)
            article.update({"source": source_name})
            self._articles.append(article)
    
    def _parse_feeds(self) -> None:
        """Parses alle the feeds from RSS_FEEDS variable using the parse_feed function"""
        for source_name, feed in RSS_FEEDS.items():
            self._parse_feed(source_name, feed)

    def get_articles(self) -> list[Article]:
        """Returns articles list"""
        return self._articles

    def print_articles(self) -> None:
        """Prints out each article"""
        for article in self._articles:
            article.print_article()