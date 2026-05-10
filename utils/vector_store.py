import faiss
import numpy as np
import pickle

from utils.catalog_loader import load_catalog
from utils.embedding_model import load_embedding_model


def create_vector_store():

    # Load catalog
    catalog = load_catalog()

    # Load embedding model
    model = load_embedding_model()

    documents = []
    metadata = []

    # Prepare text data
    for item in catalog:

        text = f"""
        Name: {item.get('name', '')}
        Description: {item.get('description', '')}
        Job Levels: {item.get('job_levels_raw', '')}
        Keys: {item.get('keys', '')}
        """

        documents.append(text)

        metadata.append({
            "name": item.get("name"),
            "url": item.get("link"),
            "description": item.get("description"),
            "keys": item.get("keys")
        })

    # Create embeddings
    embeddings = model.encode(documents)

    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    # Save index
    faiss.write_index(index, "vector_db/shl_index.faiss")

    # Save metadata
    with open("vector_db/metadata.pkl", "wb") as file:
        pickle.dump(metadata, file)

    print("Vector database created successfully!")