class Article:
    def __init__(self, source:str, title:str, description:str, pubDate:str, pubDate_parsed:str, link:str) -> None:
        self.source = source
        self.title = title
        self.description = description
        self.pubDate = pubDate
        self.pubDate_parsed = pubDate_parsed
        self.link = link