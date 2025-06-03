from fastapi import APIRouter, Body
from sim_engine import simulate_turn

router = APIRouter()

@router.post("/simulate")
def simulate(
    country_a: str = Body(..., embed=True),
    country_b: str = Body(..., embed=True),
    objective: str = Body(..., embed=True)
):
    return simulate_turn(country_a, country_b, objective)
