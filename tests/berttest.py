# Install BERTopic if you haven't already:
# pip install bertopic

from bertopic import BERTopic

# Sample documents (again, these can be a combination of title, summary, and full text)
documents = [
    "Apple unveils new iPhone with groundbreaking features.",
    "Local government passes new regulation on renewable energy.",
    "Scientists discover new species of insect in the Amazon rainforest.",
    "Tech giant releases latest software update with improved security.",
    "Political tensions rise as leaders debate new policy measures."
]

# Initialize and fit the BERTopic model
topic_model = BERTopic(language="english")
topics, probs = topic_model.fit_transform(documents)

# Display topic information
print(topic_model.get_topic_info())
