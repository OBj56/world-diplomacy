from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.sim_engine import simulate_turn



app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use exact URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TurnRequest(BaseModel):
    country_a: str
    country_b: str
    objective: str
    context: dict = {}

@app.post("/simulate")
def simulate(turn: TurnRequest):
    result = simulate_turn(
        country_a=turn.country_a,
        country_b=turn.country_b,
        objective=turn.objective,
        context=turn.context
    )
    return result
