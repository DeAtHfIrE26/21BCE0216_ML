from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text: str):
    return model.encode(text)

# app/services/search_service.py

def perform_search(query: str):
    # Example implementation
    return {"query": query, "results": "Simulated search results"}
