import json as js
import requests as rq
import bs4

class Article(dict):
    def scrape_content(self) -> (str|None):
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
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text(separator=' ', strip=True)
            self["content"] = text
            return None
        except rq.exceptions.RequestException as error:
            return f"Request error: {error}"
        except Exception as error:
            return f"Unexpected error: {error}"

    def print_article(self) -> None:
        """Prints the article values in a beautiful way"""
        print(self)

    def __str__(self):
        """Returns the article values in a beautiful way"""
        return js.dumps(dict(self), sort_keys=True, indent=4)
