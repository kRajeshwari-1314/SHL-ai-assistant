from utils.retriever import retrieve_assessments

test_queries = [
    "Java backend developer",
    "data science python test",
    "sales manager assessment"
]

for q in test_queries:
    results = retrieve_assessments(q)

    print("\nQUERY:", q)
    print("TOP RESULTS:")
    
    for r in results[:3]:
        print("-", r["name"])