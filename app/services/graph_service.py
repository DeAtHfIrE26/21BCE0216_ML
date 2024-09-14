# app/services/graph_service.py
from py2neo import Graph

# Ensure these credentials match your Neo4j instance
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
