import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent.parent
with open(BASE / "shared" / "countries.json") as f:
    COUNTRIES = json.load(f)
with open(BASE / "shared" / "strategies.json") as f:
    STRATEGIES = json.load(f)

def simulate_turn(country_a: str, country_b: str, objective: str) -> dict:
    strat_a = STRATEGIES.get(country_a, {"style": "cooperative"})
    strat_b = STRATEGIES.get(country_b, {"style": "aggressive"})

    msg_a = f"{country_a} initiates a {objective} proposal using a {strat_a['style']} strategy."
    msg_b = f"{country_b} responds with a {strat_b['style']} counter-offer."

    return {
        "a_message": msg_a,
        "b_message": msg_b,
        "next_step": "Continue negotiation or adjust strategy."
    }
