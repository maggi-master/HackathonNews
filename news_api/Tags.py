import openai
from .Tag import Tag, np

class Tags:
    def __init__(self, tags:list[str]):
        self.tags:list[Tag] = [Tag(tag) for tag in tags]

    def embedd_tags(self, model="text-embedding-3-small"):
        """Assigns a vector to all the tags using openai embedding"""
        tags = [tag.tag for tag in self]
        embeddings = openai.embeddings.create(input = tags, model=model).data
        for embedding, article in zip(embeddings, self):
            article.vector = np.array(embedding.embedding)
    
    def __str__(self):
        return str([tag.tag for tag in self])
    
    def __iter__(self):
        return iter(self.tags)
    
    def __len__(self):
        return len(self.tags)