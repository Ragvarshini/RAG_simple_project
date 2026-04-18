from pdfreader import read_pdf
from chuncker import chunk_pages,read_pdf
from embedder import embed_chunks, embed_user_query
from vectorstore import store_embeddings, search

pdf_path = r"C:/Users/ragav/OneDrive/Documents/RAG_PROJECT.PY/HR-Policy.pdf"

def run():
    pages = read_pdf(pdf_path)

    chunks = chunk_pages(pages)
    embeddings = embed_chunks(chunks)

    # store in vector DB
    index = store_embeddings(embeddings)

    # user query
    query = "leave policy"
    query_embedding = embed_user_query(query)

    results = search(index, query_embedding)

    print("\nTop relevant chunks:\n")
    for i in results:
        print(chunks[i])
        print("-" * 50)

if __name__ == "__main__":
    run()