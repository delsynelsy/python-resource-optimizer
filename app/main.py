from fastapi import FastAPI, HTTPException
from app.services.optimizer import ResourceOptimizer

app = FastAPI(title="TCS Senior Project: Resource Optimizer")

@app.get("/")
def read_root():
    return {"status": "System Online", "version": "1.0.0"}

@app.get("/optimize")
def get_optimization(hours: float, days: int):
    try:
        return ResourceOptimizer.calculate_machinery(hours, days)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))