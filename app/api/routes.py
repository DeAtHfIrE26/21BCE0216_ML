from fastapi import APIRouter
from app.services import search_service, personalization, summarization, graph_service
# app/api/routes.py
from app.services.search_service import perform_search

router = APIRouter()

@router.get("/search/{query}")
async def search(query: str):
    return search_service.perform_search(query)

@router.post("/personalize")
async def personalize(data: dict):
    return personalization.personalize_query(data['user_id'], data['query'])

@router.get("/summarize/{text}")
async def summarize(text: str):
    return summarization.summarize(text)

@router.get("/graph/query")
async def graph_query(query: str):
    return graph_service.run_query(query)
