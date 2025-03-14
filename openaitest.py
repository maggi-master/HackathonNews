import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

openAiAPIkey = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=openAiAPIkey
)

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o-mini",
)

print(response.choices[0].message)