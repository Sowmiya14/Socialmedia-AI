import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
from google import genai

# 1. Initialize Gemini AI Client (put your actual API key here)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing from .env")
    
# 2. Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Put your MySQL password here if you have one
    database="local_ai_engine"
)
cursor = db.cursor()

# 3. Simulate a local business input
business_name = "Priya's Boutique"
niche = "Boutique"
product = "Designer Festive Lehengas"

print(f"Generating AI content for {business_name}...")

# 4. Generate content using Gemini
prompt = f"Create an Instagram Reel script, 3 trending caption lines, and 5 local hashtags for a local {niche} selling {product}."

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt,
)

generated_content = response.text
print("\n--- AI Output Generated Successfully! ---")

# 5. Save the generated content into MySQL table
# Drop old table to update columns cleanly
cursor.execute("DROP TABLE IF EXISTS content_logs")

cursor.execute("""
    CREATE TABLE content_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        business_name VARCHAR(100),
        niche VARCHAR(50),
        ai_output TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Insert the data
sql = "INSERT INTO content_logs (business_name, niche, ai_output) VALUES (%s, %s, %s)"
val = (business_name, niche, generated_content)
cursor.execute(sql, val)
db.commit()

print(f"\nSaved successfully to MySQL database for {business_name}!")

# Close connections
cursor.close()
db.close()