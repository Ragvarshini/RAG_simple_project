
import faiss
import numpy as np

def store_embeddings(embeddings):
    dim = len(embeddings[0])  # embedding size
    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings))
    return index


def search(index, query_embedding, k=3):
    distances, indices = index.search(
        np.array([query_embedding]), k
    )
    return indices[0]