from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    embeddings = model.encode(chunks)
    print("Embeddings created successfully (FREE)!")
    return embeddings

def embed_user_query(query):
    return model.encode(query)