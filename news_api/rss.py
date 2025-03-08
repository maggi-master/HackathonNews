import feedparser as fp
from article import Article

class RSS:
    def __init__(self) -> None:
        pass

    def get_articles(self, source_name:str, feed:str)->list[Article]:
        parsed_feed = fp.parse(feed)
        articles = [Article(source_name, entry.title, entry.description, entry.published, entry.published_parsed, entry.link) for entry in parsed_feed.entries]
        return articles


