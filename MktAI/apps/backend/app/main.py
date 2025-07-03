from fastapi import FastAPI
from .graph import run_graph

app = FastAPI(title="MktAI Backend")

@app.post("/run_graph")
async def run_graph_endpoint(payload: dict):
    """Run LangGraph with payload as input."""
    result = await run_graph(payload)
    return {"result": result}
