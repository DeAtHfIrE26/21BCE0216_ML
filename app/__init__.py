from fastapi import FastAPI

app = FastAPI(title="Intelligent Retrieval System")

from app.api import routes  # Import routes to ensure they are registered
