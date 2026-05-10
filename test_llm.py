from utils.retriever import retrieve_assessments
from utils.llm_handler import generate_response


query = "Assessment for Java backend developer"

results = retrieve_assessments(query)

response = generate_response(query, results)

print("\nAI RESPONSE:\n")

print(response)