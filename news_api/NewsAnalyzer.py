from .Article import Article
from .Tags import Tags
import openai

class ArticleCollection:
    def __init__(self, articles:list[Article], tags:Tags):
        self._articles = articles
        self.important_keys = ['title', 'content', 'author', 'published', 'source', 'link']
        self.tags = tags

    def generate_email(self, model="gpt-4o-mini") -> str:
        """
        Constructs a prompt using the provided articles, asking ChatGPT to analyze,
        summarize critically, and then write an email based on the summary, referencing the articles.
        """
        formatted_articles = ""
        for articleIndex, article in enumerate(self, start=1):
            formatted_articles += f"\nArtikkel nr. {articleIndex}\n"
            formatted_articles += f"Relvante temaer {str(article.tags)}\n"
            for key in self.important_keys:
                formatted_articles += str(article.get(key, ''))+"\n"
        
        promt = f"""
Analyser og oppsummer følgende nyhetsartikler. Vurder kritisk vinkling, troverdighet og mulige mangler ved dekningen.

Nyhetene for i dag:
Oppsummer de viktigste hendelsene og trekk frem eventuelle motstridende synspunkter. Syntetiser informasjonen på tvers av artiklene for å gi en helhetlig oversikt over de ulike temaene.

Kategoriser nyhetene etter temane {str(self.tags)}. Du kan kombinere temaer hvis de er relvante til hverandre. Du kan fjerne temaer hvis det ikke er noen nyheter om temaene. 
Bruk hyperlenker til artiklene direkte i teksten for å referere til kilder.
Analyser vinkling ved å sammenligne dekningen fra ulike kilder, peke på skjevheter og identifisere eventuelle manglende perspektiver.
Vær presis og objektiv, men også kritisk der det er nødvendig.

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