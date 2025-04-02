from bs4 import BeautifulSoup
import requests as rq
import logging as log

class HTMLParser():
    def __init__(self, url:str=None) -> None:
        self._logger = log.getLogger(__name__)
        self._logger.setLevel(log.ERROR)
        self._url = url
        self._domain = self._get_domain(url)
        self._soup = None
        self._html = None
        self._content = None
        self._content_type = None

    def get_content(self) -> str:
        """Returns content found from html scraping"""
        return self._content

    def scrape_content(self) -> None:
        """Runs relevants functions to scrape content"""
        self._fetch_html()
        self._parse_html() 

    def _fetch_html(self) -> None:
        """Fetches raw HTML"""
        try:
            response = rq.get(self._url)
            response.raise_for_status()
            self._html = response.text
            self._content_type = response.headers.get('Content-Type', '')
        except rq.exceptions.RequestException as error:
            self._logger.error(f"Error fetching HTML from {self._url}: {error}")

    def _parse_html(self) -> None:
        """Parses HTML using BeautifulSoup if domain is accounted for"""
        if "html" in self._content_type:
            self._soup = BeautifulSoup(self._html, 'html.parser')
        elif "xml" in self._content_type:
            self._soup = BeautifulSoup(self._html, 'xml')
        else:
            self._logger.error(f"Unknown content type, cannot parse type {self._content_type}")

        if self._domain == "www.nrk.no":
            self._parse_content("article-body lp_articlebody text-body text-body-sans-serif container-widget-content nostack cf")
        elif self._domain == "www.dagbladet.no":
            self._parse_content("bodytext large-12 small-12 medium-12")
        elif self._domain == "www.vg.no":
            self._parse_content("article-body")
        elif self._domain == "www.reuters.com":
            self._parse_content("article-body__content__17Yit")
        elif self._domain == "e24.no":
            self._parse_content("article-wrapper-eM4V3y")
        else:
            self._logger.error(f"Unknown domain, cannot parse from {self._domain}")

    def _get_domain(self, url:str) -> str:
        """Strips URL to get domain"""
        domain = url
        if "://" in domain:
            domain = domain.split("://")[1]
        if "/" in domain:
            domain = domain.split("/")[0]
        return domain

    def _parse_content(self, text_body_name):
        article = self._soup.find("div", class_=text_body_name)
        if article:
            self._content = article.get_text(separator=" ", strip=True)
            self._content = self._content.replace("\n", " ")
            self._content = " ".join(self._content.split())
        else:
            self._logger.error(f"Could not find article content for {self._url}")


    def print_html(self) -> None:
        """Prints out HTML for debugging"""
        print(self)

    def __str__(self) -> str:
        return self._soup.prettify()