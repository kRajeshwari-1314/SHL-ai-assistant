import requests
import json
import re

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(url)

# Get raw text
raw_text = response.text

# Remove invalid control characters
clean_text = re.sub(r'[\x00-\x1F\x7F]', '', raw_text)

# Convert cleaned text to JSON
data = json.loads(clean_text)

# Save cleaned catalog
with open("data/shl_catalog.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Catalog downloaded and cleaned successfully!")