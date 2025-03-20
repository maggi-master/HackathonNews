import json as js
import requests as rq
from HTML_scrapper import HTML

class Article(dict):
    def get_html(self) -> (str|None):
        """
        Scrapes content from the url stored in "link".

        Returns:
            str: Error message if an error has occured
            None: The operation was successfull
        
        """
        if "link" not in self:
            return "Attribute error: No URL provided"
        
        try:
            response = rq.get(self["link"])
            response.raise_for_status()
            self.html = response.text
            return None
        except rq.exceptions.RequestException as error:
            return f"Request error: {error}"
        except Exception as error:
            return f"Unexpected error: {error}"
    
    def get_content(self):
        self.get_html()
        scrapper = HTML()
        scrapper.pretty_print()
        self["content"] = scrapper.get_content()

    def print_article(self) -> None:
        """Prints the article values in a beautiful way"""
        print(self)

    def __str__(self):
        """Returns the article values in a beautiful way"""
        return js.dumps(dict(self), sort_keys=True, indent=4)