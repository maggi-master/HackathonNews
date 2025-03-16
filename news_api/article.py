class Article:
    def __init__(self, source_name:str, title:str, description:str, link:str, pubDate:str=None, pubDate_parsed:str=None) -> None:
        self.source = source_name
        self.title = title
        self.description = description
        self.link = link
        self.pubDate = pubDate
        self.pubDate_parsed = pubDate_parsed