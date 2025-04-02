import json as js
from .html_parser import HTMLParser
import numpy as np

class Article(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vector:np.ndarray = None
    
    def update_content(self):
        """Updates content by scraping from stored URL"""
        url = self.get("link", '')
        html_parser = HTMLParser(url)
        html_parser.scrape_content()
        self["content"] = html_parser.get_content()

    def __str__(self):
        """Returns the article values in a beautiful way"""
        return js.dumps(dict(self), sort_keys=True, indent=4, ensure_ascii=False)