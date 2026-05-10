import faiss
import pickle
import numpy as np

from utils.embedding_model import load_embedding_model


# Load vector database
index = faiss.read_index("vector_db/shl_index.faiss")

# Load metadata
with open("vector_db/metadata.pkl", "rb") as file:
    metadata = pickle.load(file)

# Load embedding model
model = load_embedding_model()


def retrieve_assessments(query, top_k=5):

    # Convert query to embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        results.append(metadata[idx])

    return results