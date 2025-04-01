import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Example data: article vectors and a search vector.
articles = np.array([
    [0,0],
    [0, 1],
    [1, 0],
    [-1,-1]
])

tags = np.array([
    [1, 0.1],
    [0.5, 0.6],
    [0.2, 1],
])

print(articles)
print(tags)
print()

# Compute cosine similarities (each value corresponds to an article)
similarities = cosine_similarity(tags, articles)
print(similarities)

# Define your similarity threshold (e.g., 0.99 for high similarity)
threshold = 0.97
# Filter articles based on the threshold

for tagIndex, tagSimilarities in enumerate(similarities):
    for articleIndex, similarity in enumerate(tagSimilarities):
        print(tagIndex, articleIndex, similarity)
    print()