from .Article import Article

class ArticleCollection:
    def __init__(self, articles:list[Article]):
        self._articles = articles