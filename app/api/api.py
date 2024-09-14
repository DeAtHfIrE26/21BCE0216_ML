# api.py
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import json
from cache import cache_set, cache_get
from database import get_neo4j_graph, get_sqlite_connection

app = FastAPI()

class SearchRequest(BaseModel):
    text: str
    top_k: int = 10
    threshold: float = 0.5

def log_request(user_id: str):
    connection = get_sqlite_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO users (user_id, request_count) VALUES (?, COALESCE((SELECT request_count FROM users WHERE user_id = ?), 0) + 1)",
        (user_id, user_id)
    )
    connection.commit()
    request_count = cursor.execute("SELECT request_count FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
    if request_count > 5:
        raise HTTPException(status_code=429, detail="Too many requests")

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/search")
def search(request: SearchRequest, user_id: str):
    log_request(user_id)
    
    cache_key = f"search:{user_id}:{request.text}:{request.top_k}:{request.threshold}"
    cached_result = cache_get(cache_key)
    
    if cached_result:
        return json.loads(cached_result)
    
    graph = get_neo4j_graph()
    query = """
    MATCH (n)
    WHERE n.text CONTAINS $text
    RETURN n
    LIMIT $top_k
    """
    results = graph.run(query, text=request.text, top_k=request.top_k).data()
    
    result = {"results": results}
    cache_set(cache_key, json.dumps(result))
    
    return result
