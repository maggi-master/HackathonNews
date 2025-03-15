from gensim import corpora, models, similarities

# Sample documents
documents = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement"
]

# Tokenize documents (basic lowercasing and splitting)
texts = [doc.lower().split() for doc in documents]

# Create a dictionary mapping words to ids
dictionary = corpora.Dictionary(texts)

# Convert documents into bag-of-words vectors
corpus = [dictionary.doc2bow(text) for text in texts]

# Build a TF-IDF model and transform the corpus
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

# Create a similarity index from the TF-IDF vectors
index = similarities.MatrixSimilarity(corpus_tfidf, num_features=len(dictionary))

# Create a query document and convert it into the same vector space
query_doc = "computer interface system"
query_bow = dictionary.doc2bow(query_doc.lower().split())
query_tfidf = tfidf[query_bow]

# Compute similarities between the query and each document in the corpus
sims = index[query_tfidf]
print(list(enumerate(sims)))
