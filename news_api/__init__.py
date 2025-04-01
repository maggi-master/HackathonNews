from .Articles import Articles
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.api_key)