from .Article import Article
from .Tags import Tags
import openai

class ArticleCollection:
    def __init__(self, articles:list[Article], tags:Tags):
        self._articles = articles
        self.important_keys = ['content', 'author', 'published', 'source', 'link']
        self.tags = tags

    def generate_email(self, model="gpt-4o-mini") -> str:
        """
        Constructs a prompt using the provided articles, asking ChatGPT to analyze,
        summarize critically, and then write an email based on the summary, referencing the articles.
        """
        formatted_articles = ""
        for article in self:
            formatted_articles += f"Tittel: {article["title"]}\n"
            formatted_articles += f"Relvante temaer {str(article.tags)}\n"
            for key in self.important_keys:
                formatted_articles += str(article.get(key, ''))+"\n"
        
        promt = f"""
Analyser og oppsummer følgende nyhetsartikler. Fokuser på å beskrive hovedinnholdet og de viktigste hendelsene, og syntetiser informasjonen på tvers av artiklene for å gi en helhetlig oversikt over de ulike temaene.

Nyhetene for i dag:
Oppsummer de sentrale hendelsene, og fremhev eventuelle motstridende synspunkter. Kategoriser nyhetene etter temaene {str(self.tags)}. Du kan kombinere temaer hvis de er relevante for hverandre, og utelate temaer som ikke har tilstrekkelig dekning.

Bruk hyperlenker til artiklene direkte i teksten for å referere til kildene.

Kildeliste:
Oppgi en liste over de analyserte artiklene med deres titler og lenker.

#### Artikler til analyse:
{formatted_articles}
"""


        messages = [
            {"role": "system", "content": "Du er en AI-assistent som kritisk oppsummerer nyhetsartikler på norsk."},
            {"role": "user", "content": promt}
        ]

        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7  # Adjust temperature for creativity vs. determinism
        )

        return response.choices[0].message.content

    def __iter__(self):
        return iter(self._articles)