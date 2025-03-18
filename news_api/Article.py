import json

class Article(dict):
    def print_article(self):
        """Prints the article values in a beutiful way"""
        print(json.dumps(dict(self), sort_keys=True, indent=4))
