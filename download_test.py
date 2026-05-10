from utils.catalog_loader import load_catalog


data = load_catalog()

print("Catalog loaded successfully!")

print("Total assessments:", len(data))

print("\nFirst assessment:\n")

print(data[0])