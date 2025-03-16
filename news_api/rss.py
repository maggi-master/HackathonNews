import feedparser as fp
from rss_feeds import RSS_FEEDS
from article import Article

class RSS:
    def __init__(self) -> None:
        self._articles = []
        for source_name, feed in RSS_FEEDS.items():
            self._parse_feed(source_name, feed)

    def _parse_feed(self, source_name:str, feed:str) -> None:
        """Parses single feed and appends to articles list"""
        parsed_feed = fp.parse(feed)
        for entry in parsed_feed.entries:
            if hasattr(entry, "published"):
                new_article = Article(source_name, entry.title, entry.description, entry.link, entry.published, entry.published_parsed)
            else:
                new_article = Article(source_name, entry.title, entry.description, entry.link)                
            self._articles.append(new_article)
        
    def get_articles(self) -> list[Article]:
        """Returns articles list"""
        return self._articles

if __name__ == "__main__":
    rss = RSS()
    for article in rss.get_articles():
        print(f"{article.source}: {article.title} ({article.link})")