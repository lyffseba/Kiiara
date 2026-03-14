"""
Strategy configuration for financial autoresearch.
This file is meant to be modified by the AI agent.
"""

import json
from financial_sim import generate_synthetic_profile, evaluate_strategy

# Default strategy (baseline)
STRATEGY = {
    "food": 0.15,  # 15% of income
    "transportation": 0.10,
    "entertainment": 0.05,
    "shopping": 0.05,
    "healthcare": 0.03,
    "savings": 0.20,
    "investment": 0.10,
}


def main():
    """Run evaluation of current strategy."""
    profile = generate_synthetic_profile(seed=42)  # fixed seed for consistency

    evaluation = evaluate_strategy(STRATEGY, profile)

    # Print results in parseable format
    print("---")
    print(f"score:            {evaluation['score']:.3f}")
    print(f"total_wealth:     {evaluation['total_wealth']:.2f}")
    print(f"goal_achievement: {evaluation['goal_achievement']:.3f}")
    print(f"consistency:      {evaluation['consistency']:.3f}")
    print(f"negative_months:  {evaluation['negative_months']}")
    print()
    print("Strategy allocation:")
    for category, alloc in STRATEGY.items():
        print(f"  {category}: {alloc:.1%}")

    # Also output JSON for easy parsing
    result_json = {
        "score": evaluation["score"],
        "total_wealth": evaluation["total_wealth"],
        "goal_achievement": evaluation["goal_achievement"],
        "consistency": evaluation["consistency"],
        "negative_months": evaluation["negative_months"],
        "strategy": STRATEGY,
    }
    with open("last_run.json", "w") as f:
        json.dump(result_json, f, indent=2)


if __name__ == "__main__":
    main()
