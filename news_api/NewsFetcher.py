import feedparser as fp
import openai
import copy
from .rss_feeds import RSS_FEEDS
from .Article import Article, np
from sklearn.metrics.pairwise import cosine_similarity
from .Tags import Tags

class FetchNews:
    def __init__(self) -> None:
        self._articles:list[Article] = []
        self._parse_feeds()
        self._embedd_articles()

    def _parse_feed(self, source_name:str, feed:str) -> None:
        """Parses single feed and appends to articles list"""
        parsed_feed = fp.parse(feed)
        for entry in parsed_feed.entries:
            article = Article(entry)
            article.update({"source": source_name})
            self._articles.append(article)

    def _parse_feeds(self) -> None:
        """Parses alle the feeds from RSS_FEEDS variable using the parse_feed function"""
        for source_name, feed in RSS_FEEDS.items():
            self._parse_feed(source_name, feed)

    def get_articles(self) -> list[Article]:
        """Returns articles list"""
        return self._articles

    def print_articles(self) -> None:
        """Prints out each article"""
        for article in self:
            print(article)

    def _filter_articles(self) -> None:
        self._articles = [article for article in self if article["summary"] != ""]

    def _embedd_articles(self, model="text-embedding-3-small"):
        """Assigns a vector to all the articles based on the summary of the article using openai embedding"""
        self._filter_articles()
        summaries = [article["summary"] for article in self]
        embeddings = openai.embeddings.create(input = summaries, model=model).data
        for embedding, article in zip(embeddings, self):
            article.vector = np.array(embedding.embedding)

    def search(self, tags:Tags, threshold:float = 0.3) -> list[Article]:
        """Retuns list of articles if the maximum cosine of the vectors to the articles and tags are equal or greater than the threshold"""
        articlesV = np.array([article.vector for article in self])
        tagsV = np.array([tag.vector for tag in tags])
        similaritiesMatrix = cosine_similarity(articlesV, tagsV)
        articles = []
        for article, similarities in zip(self._articles, similaritiesMatrix):
            relvant = False
            relvantTags = []
            for tag, similarity in zip(tags, similarities):
                if similarity >= threshold:
                    relvant = True
                    if "content" not in article: #Checks if already scraped the website for the content
                        article.update_content()
                    tagCopy = copy.deepcopy(tag)
                    tagCopy.similarity = similarity
                    relvantTags.append(tagCopy)
            relvantArticle = Article(article)
            relvantArticle.tags = Tags(relvantTags)
            if relvant:
                articles.append(relvantArticle)
        return articles

    def __iter__(self):
        return iter(self._articles)

    def __len__(self):
        return len(self._articles)