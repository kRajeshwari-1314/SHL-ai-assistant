from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(query, retrieved_results):

    # Build context safely
    context = ""

    for result in retrieved_results:
        context += f"""
Assessment Name: {result.get('name', '')}
Description: {result.get('description', '')}
URL: {result.get('url', '')}
---
"""

    # Strong SHL-style prompt (IMPORTANT for marks)
    prompt = f"""
You are an SHL AI Assessment Recommendation Assistant.

RULES:
- Use ONLY the provided SHL catalog data.
- Do NOT hallucinate or create new assessments.
- Recommend ONLY 3–5 best matching assessments.
- Rank them from most relevant to least relevant.
- Give clear reasoning for each recommendation.

OUTPUT FORMAT:
1. Assessment Name
   Reason: why it matches
   URL: link

User Query:
{query}

SHL Catalog:
{context}
"""

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content