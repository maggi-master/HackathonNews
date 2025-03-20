import json as js
from .html_parser import HTMLParser

class Article(dict):
    def update_content(self):
        """Updates content by scraping from stored URL"""
        url = self.get("link", '')
        html_parser = HTMLParser(url)
        html_parser.scrape_content()
        self["content"] = html_parser.get_content()

    def print_article(self) -> None:
        """Prints the article values in a beautiful way"""
        print(self)

    def __str__(self):
        """Returns the article values in a beautiful way"""
        return js.dumps(dict(self), sort_keys=True, indent=4)