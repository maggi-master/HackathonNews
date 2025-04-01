from .Tag import Tag, np
import openai

class Tags:
    def __init__(self):
        self._tags:list[Tag]

    def embedd_tags(self, model="text-embedding-3-small"):
        """Assigns a vector to all the tags using openai embedding"""
        tags = [tag.tag for tag in self._tags]
        embeddings = openai.embeddings.create(input = tags, model=model).data
        for embedding, article in zip(embeddings, self._tags):
            article.vector = np.array(embedding.embedding)