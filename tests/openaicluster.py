import os
from dotenv import load_dotenv
import openai
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

articles = [
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

embeddings = openai.embeddings.create(input = articles, model="text-embedding-ada-002").data
embeddingsNumbers = np.array([embedding.embedding for embedding in embeddings])

# Determine the number of clusters
n_clusters = 3
clustering_model = AgglomerativeClustering(n_clusters=n_clusters, metric="cosine", linkage="average")
clusters = clustering_model.fit_predict(embeddingsNumbers)

# Print grouped articles
cluster_groups = {i: [] for i in range(n_clusters)}
for i, cluster_id in enumerate(clusters):
    cluster_groups[cluster_id].append(articles[i])

print("\nGrouped News Articles:\n")
for cluster_id, articles in cluster_groups.items():
    print(f"Group {cluster_id + 1}:")
    for article in articles:
        print(f"  - {article}")
    print()