from .Article import Article
import openai

class ArticleCollection:
    def __init__(self, articles:list[Article]):
        self._articles = articles
        self.important_keys = ['title', 'content', 'author', 'published', 'source', 'link']


    def generate_email(self, model="gpt-4o-mini") -> str:
        """
        Constructs a prompt using the provided articles, asking ChatGPT to analyze,
        summarize critically, and then write an email based on the summary, referencing the articles.
        """
        formatted_articles = ""
        for articleIndex, article in enumerate(self, start=1):
            formatted_articles += f"\nArtikkel nr. {articleIndex}\n"
            for key in self.important_keys:
                formatted_articles += str(article.get(key, ''))+"\n"
        
        promt = f"""
Analyser og oppsummer følgende nyhetsartikler. Vær kritisk i din analyse og vurder vinkling, troverdighet og mulige mangler ved dekningen.

Start med her er Nyhetene for idag, og slutt med en kildeliste.

Når du oppsummerer, trekk ut de viktigste poengene og eventuelle motstridende synspunkter presentert i artiklene.

**Referer tydelig** til de spesifikke artiklene (bruk tittel, kilde eller lenke/identifikator som oppgitt) når du henter informasjon eller kritikk.

Ikke bare list opp hva hver artikkel sier; syntetiser informasjonen til en sammenhengende oversikt over temaet(ene) som dekkes.

Her er den relevante informasjonen fra artiklene:

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