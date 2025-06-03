import json
from pathlib import Path
import random

BASE = Path(__file__).resolve().parent.parent.parent.parent

with open(BASE / "shared" / "countries.json") as f:
    COUNTRIES = json.load(f)
with open(BASE / "shared" / "strategies.json") as f:
    STRATEGIES = json.load(f)

def simulate_turn(country_a: str, country_b: str, objective: str, context: dict = None) -> dict:
    context = context or {}
    history = context.get("history", [])

    strat_a = STRATEGIES.get(country_a, {"style": "cooperative", "aggressiveness": 0.3, "bluff": 0.1})
    strat_b = STRATEGIES.get(country_b, {"style": "aggressive", "aggressiveness": 0.7, "bluff": 0.3})

    profile_a = COUNTRIES.get(country_a, {})
    profile_b = COUNTRIES.get(country_b, {})

  
    tone_a = "cautiously proposes" if strat_a["style"] == "cooperative" else \
             "firmly demands" if strat_a["aggressiveness"] > 0.6 else \
             "proposes"

    resource_a = random.choice(profile_a.get("resources", ["influence"]))
    goal_a = random.choice(profile_a.get("goals", ["mutual benefit"]))

    msg_a = f"{country_a} {tone_a} a {objective} deal centered around its strength in {resource_a}, aiming to achieve '{goal_a}'."


    if strat_a["bluff"] > 0.5:
        msg_a += f" Privately, {country_a} plans to ignore parts of the deal."


    tone_b = "agrees in principle" if strat_b["style"] == "cooperative" else \
             "outright rejects the deal" if strat_b["aggressiveness"] > 0.8 else \
             "responds with skepticism"

    resource_b = random.choice(profile_b.get("resources", ["market access"]))
    goal_b = random.choice(profile_b.get("goals", ["influence"]))

    msg_b = f"{country_b} {tone_b}, emphasizing its own leverage in {resource_b} and prioritizing '{goal_b}'."

    if strat_b["bluff"] > 0.5:
        msg_b += f" However, behind closed doors, {country_b} considers a strategic deception."


    history.append(f"🇦 {msg_a}")
    history.append(f"🇧 {msg_b}")

    return {
        "a_message": msg_a,
        "b_message": msg_b,
        "next_step": "Continue negotiation or propose a revision.",
        "history": history
    }
