import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Generate sample data
# Here we create a dataset with 300 samples and 4 centers
X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# 2. Perform Agglomerative Clustering using a distance threshold
# Setting n_clusters=None and a distance_threshold lets the algorithm decide
# the number of clusters based on the specified threshold.
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=8, linkage='ward')
labels = clustering.fit_predict(X)

# 3. Visualize the clustering results
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
plt.title('Agglomerative Clustering with Distance Threshold')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# 4. (Optional) Plot the dendrogram to inspect the hierarchical structure
# The linkage matrix is computed using the 'ward' method.
linked = linkage(X, method='ward')

plt.figure(figsize=(10, 5))
dendrogram(linked,
           truncate_mode='level',  # display only the top levels of the tree
           p=3)                    # number of levels to show
plt.title('Dendrogram for Agglomerative Clustering')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()
