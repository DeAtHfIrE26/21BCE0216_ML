import logging
from py2neo import Graph

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Replace with your actual Neo4j credentials and address
uri = "neo4j+s://06d6e64a.databases.neo4j.io"
user = "neo4j"
password = "vbpY2b3x8cLM5u1jPXk5qMyWt0DNwg6nHTGYv6wVc78"

try:
    graph = Graph(uri, auth=(user, password))
    result = graph.run("MATCH (n) RETURN count(n) AS node_count").data()
    print(result)
except Exception as e:
    print(f"Error: {e}")
