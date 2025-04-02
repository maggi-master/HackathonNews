from .Tags import Tags
from .NewsFetcher import FetchNews
from .NewsAnalyzer import ArticleCollection
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")