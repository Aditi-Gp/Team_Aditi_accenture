# api/main.py — FastAPI App Entry Point (Updated for Multi-Agent System)
# http://localhost:8000
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.agent_orchestrator import orchestrate
from db.database import save_orchestration_result
from typing import Dict

app = FastAPI(title="Retail Inventory Multi-Agent AI System")

class OrchestratorRequest(BaseModel):
    product_id: int
    store_id: int

@app.post("/orchestrate")
def run_orchestration(req: OrchestratorRequest):
    try:
        result: Dict = orchestrate(req.product_id, req.store_id)
        save_orchestration_result(req.product_id, req.store_id, result)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
