from backend.loader import load_nodes
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/nodes")
def get_nodes():
    return load_nodes()
