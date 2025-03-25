from gensim import corpora, models
from gensim.similarities import MatrixSimilarity
from sklearn.cluster import AgglomerativeClustering
import numpy as np

news_articles = [
    "Apple unveils the iPhone 15 with a titanium design and USB-C",
    "Samsung announces Galaxy S24 with advanced AI camera features",
    "Google introduces new AI chatbot to rival ChatGPT",
    "Tesla launches new electric truck with increased battery range",
    "Ford reveals its latest hybrid car model for 2025",
    "Scientists discover a new exoplanet that could support life",
    "NASA's James Webb Telescope captures stunning deep-space images",
    "Major breakthrough in quantum computing promises faster processing",
    "Bitcoin surges past $50,000 as investors pile into crypto",
    "Ethereum set to implement major upgrade improving scalability",
]

# Tokenize articles
texts = [article.lower().split() for article in news_articles]

# Create dictionary and corpus
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# Apply TF-IDF
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# Compute similarity matrix
index = MatrixSimilarity(corpus_tfidf)
similarities = np.array([index[doc] for doc in corpus_tfidf])

# Use Agglomerative Clustering to group articles
n_clusters = 5  # Adjust based on expected topics
clustering_model = AgglomerativeClustering(n_clusters=n_clusters, metric="cosine", linkage="average")
clusters = clustering_model.fit_predict(similarities)

# Print grouped articles
cluster_groups = {i: [] for i in range(n_clusters)}
for i, cluster_id in enumerate(clusters):
    cluster_groups[cluster_id].append(news_articles[i])

print("\nGrouped News Articles:\n")
for cluster_id, articles in cluster_groups.items():
    print(f"Group {cluster_id + 1}:")
    for article in articles:
        print(f"  - {article}")
    print()
