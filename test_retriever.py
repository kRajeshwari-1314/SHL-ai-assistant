from utils.retriever import retrieve_assessments


query = "Java developer assessment"

results = retrieve_assessments(query)

print("\nTop Matching Assessments:\n")

for i, result in enumerate(results, start=1):

    print(f"{i}. {result['name']}")

    print("URL:", result["url"])

    print("Description:", result["description"])

    print("-" * 80)