import os
from google import genai
from dotenv client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
import load_dotenv

load_dotenv()

# Initialize the Gemini client (paste your API key inside the quotes)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing from .env")

# Let's test it with a sample local business input
niche = "Boutique"
product = "New festive saree collection"

prompt = f"Create an Instagram Reel script, 3 trending caption lines, and 5 local hashtags for a local {niche} selling {product}."

# Ask Gemini to generate the content using the fast 2.5 flash model
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt,
)

print("--- AI Generated Reel Kit ---")
print(response.text)