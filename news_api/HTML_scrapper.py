from bs4 import BeautifulSoup

class HTML:
    def __init__(self, html_doc:str, source:str):
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.source = source
    
    def pretty_print(self):
        print(self.soup.prettify())

    def get_content(self):
        if self.source=="nrk.no":
            return self.nrk()

    def nrk(self):
        return self.soup.find("div", {"class": "article-body"}).get_text()