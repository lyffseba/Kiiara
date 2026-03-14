"""
Demo of financial autoresearch optimization loop.
Simulates the agent experimenting with different strategies.
"""

import json
import random
import sys
from typing import Dict, List
from .financial_sim import generate_synthetic_profile, evaluate_strategy


def run_autoresearch_demo(iterations: int = 5, seed: int = 42) -> Dict:
    """
    Run a simplified autoresearch optimization demo.
    Returns best strategy and optimization history.
    """
    profile = generate_synthetic_profile(seed=seed)
    random.seed(seed + 1)

    # Baseline strategy
    best_strategy = {
        "food": 0.15,
        "transportation": 0.10,
        "entertainment": 0.05,
        "shopping": 0.05,
        "healthcare": 0.03,
        "savings": 0.20,
        "investment": 0.10,
    }

    best_score = -float("inf")
    history = []

    for i in range(iterations):
        # Generate a random tweak to best strategy
        strategy = best_strategy.copy()

        # Randomly adjust 1-3 categories
        categories = list(strategy.keys())
        num_changes = random.randint(1, 3)
        for _ in range(num_changes):
            cat = random.choice(categories)
            if cat in ["savings", "investment"]:
                # Increase/decrease by 2-5%
                delta = random.uniform(-0.05, 0.05)
            else:
                # Expense categories: adjust within reasonable bounds
                delta = random.uniform(-0.03, 0.03)
            strategy[cat] = max(0.01, min(0.5, strategy[cat] + delta))

        # Normalize to ensure sum <= 1.0
        total = sum(strategy.values())
        if total > 1.0:
            # Scale down proportionally
            scale = 0.95 / total  # leave 5% buffer
            for cat in strategy:
                strategy[cat] *= scale

        # Evaluate
        evaluation = evaluate_strategy(strategy, profile)
        score = evaluation["score"]

        # Record result
        entry = {
            "iteration": i,
            "strategy": strategy,
            "score": score,
            "total_wealth": evaluation["total_wealth"],
            "goal_achievement": evaluation["goal_achievement"],
            "improved": score > best_score,
        }
        history.append(entry)

        # Update best if improved
        if score > best_score:
            best_score = score
            best_strategy = strategy
            print(f"Iteration {i}: New best score {score:.3f}")
        else:
            print(f"Iteration {i}: Score {score:.3f} (no improvement)")

    # Final evaluation of best strategy
    final_eval = evaluate_strategy(best_strategy, profile)

    return {
        "best_strategy": best_strategy,
        "best_score": best_score,
        "final_evaluation": final_eval,
        "history": history,
        "profile": {
            "monthly_income": profile.monthly_income,
            "savings_goal": profile.savings_goal,
            "investment_return": profile.investment_return,
        },
    }


def main():
    """Run the demo and output results."""
    print("Financial Autoresearch Demo")
    print("=" * 40)

    results = run_autoresearch_demo(iterations=5)

    print("\nOptimization Complete!")
    print(f"Best Score: {results['best_score']:.3f}")
    print("\nBest Strategy:")
    for cat, alloc in results["best_strategy"].items():
        print(f"  {cat}: {alloc:.1%}")

    print(f"\nTotal Wealth: ${results['final_evaluation']['total_wealth']:.2f}")
    print(f"Goal Achievement: {results['final_evaluation']['goal_achievement']:.1%}")

    # Save detailed results
    with open("autoresearch_results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Also output summary for potential API integration
    summary = {
        "best_strategy": results["best_strategy"],
        "score": results["best_score"],
        "improvement": results["best_score"] - results["history"][0]["score"],
        "iterations": len(results["history"]),
        "recommendation": "Increase savings and investment allocations while maintaining reasonable lifestyle expenses.",
    }

    print("\nRecommendation for Kiiara:")
    print(f"  {summary['recommendation']}")

    return summary


if __name__ == "__main__":
    main()
