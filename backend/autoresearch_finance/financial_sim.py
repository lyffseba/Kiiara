"""
Financial simulation for autoresearch optimization.
Simulates a year of budgeting with given strategy parameters.
"""

import json
import random
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class FinancialProfile:
    """User's financial profile."""

    monthly_income: float
    fixed_expenses: Dict[str, float]  # rent, utilities, etc.
    variable_expense_ranges: Dict[str, Tuple[float, float]]  # category -> (min, max)
    savings_goal: float  # target annual savings
    investment_return: float  # annual expected return (0.05 = 5%)


def generate_synthetic_profile(seed: int = 42) -> FinancialProfile:
    """Generate a realistic financial profile."""
    random.seed(seed)
    monthly_income = random.uniform(4000, 8000)
    fixed_expenses = {
        "rent": monthly_income * 0.3,
        "utilities": random.uniform(100, 200),
        "insurance": random.uniform(150, 300),
        "subscriptions": random.uniform(50, 150),
    }
    variable_expense_ranges = {
        "food": (200.0, 600.0),
        "transportation": (100.0, 400.0),
        "entertainment": (100.0, 500.0),
        "shopping": (100.0, 800.0),
        "healthcare": (50.0, 300.0),
    }
    savings_goal = monthly_income * 12 * 0.2  # 20% savings goal
    investment_return = random.uniform(0.03, 0.08)

    return FinancialProfile(
        monthly_income=monthly_income,
        fixed_expenses=fixed_expenses,
        variable_expense_ranges=variable_expense_ranges,
        savings_goal=savings_goal,
        investment_return=investment_return,
    )


def simulate_month(
    profile: FinancialProfile, strategy: Dict[str, float]
) -> Dict[str, float]:
    """
    Simulate one month given strategy allocations.
    Strategy keys: food, transportation, entertainment, shopping, healthcare, savings, investment
    Values: percentages of monthly_income (should sum to <= 1.0)
    """
    # Apply variable expenses within allocated budget
    actual_expenses = {}
    for category, (min_exp, max_exp) in profile.variable_expense_ranges.items():
        allocated = strategy.get(category, 0.0) * profile.monthly_income
        # Spend between min and allocated, but not more than max
        actual = random.uniform(min_exp, min(allocated, max_exp))
        actual_expenses[category] = actual

    # Fixed expenses
    total_fixed = sum(profile.fixed_expenses.values())

    # Calculate remaining income
    total_variable = sum(actual_expenses.values())
    total_expenses = total_fixed + total_variable

    # Savings and investment allocations
    savings_alloc = strategy.get("savings", 0.0) * profile.monthly_income
    investment_alloc = strategy.get("investment", 0.0) * profile.monthly_income

    # Actual savings (cannot exceed remaining income)
    remaining = profile.monthly_income - total_expenses
    actual_savings = min(savings_alloc, remaining)
    remaining -= actual_savings
    actual_investment = min(investment_alloc, remaining)

    return {
        "income": profile.monthly_income,
        "fixed_expenses": total_fixed,
        "variable_expenses": total_variable,
        "savings": actual_savings,
        "investment": actual_investment,
        "surplus": remaining - actual_investment,
    }


def evaluate_strategy(
    strategy: Dict[str, float], profile: FinancialProfile, months: int = 12
) -> Dict[str, Any]:
    """
    Evaluate a financial strategy over multiple months.
    Returns metrics including total savings, goal achievement, and composite score.
    """
    total_savings = 0.0
    total_investment = 0.0
    monthly_results = []

    for month in range(months):
        result = simulate_month(profile, strategy)
        total_savings += result["savings"]
        total_investment += result["investment"]
        monthly_results.append(result)

    # Calculate investment growth (simple annual return prorated)
    investment_growth = total_investment * (profile.investment_return / 12 * months)
    total_wealth = total_savings + total_investment + investment_growth

    # Goal achievement (percentage of savings goal met)
    goal_achievement = (
        min(1.0, total_savings / profile.savings_goal)
        if profile.savings_goal > 0
        else 1.0
    )

    # Consistency penalty (months with negative surplus)
    negative_months = sum(1 for r in monthly_results if r["surplus"] < 0)
    consistency = 1.0 - (negative_months / months)

    # Composite score (higher is better)
    score = (
        0.4 * goal_achievement
        + 0.3 * (total_wealth / (profile.monthly_income * months))  # wealth ratio
        + 0.2 * consistency
        + 0.1 * (1.0 - sum(strategy.values()))  # bonus for not allocating all income
    )

    return {
        "total_savings": total_savings,
        "total_investment": total_investment,
        "investment_growth": investment_growth,
        "total_wealth": total_wealth,
        "goal_achievement": goal_achievement,
        "consistency": consistency,
        "negative_months": negative_months,
        "score": score,
        "monthly_results": monthly_results,
    }


def optimize_strategy(
    profile: FinancialProfile, iterations: int = 10
) -> List[Dict[str, Any]]:
    """
    Run simple random optimization to find better strategies.
    Returns list of (strategy, score) sorted by score descending.
    """
    results = []
    best_score = -float("inf")
    best_strategy = None

    for i in range(iterations):
        # Generate random strategy
        categories = [
            "food",
            "transportation",
            "entertainment",
            "shopping",
            "healthcare",
            "savings",
            "investment",
        ]
        strategy = {}
        remaining = 1.0

        # Allocate random percentages (ensuring sum <= 1.0)
        for cat in categories[:-1]:  # leave some for last category
            alloc = random.uniform(0.01, remaining * 0.5)
            strategy[cat] = alloc
            remaining -= alloc
        strategy[categories[-1]] = remaining  # allocate remaining to last category

        # Evaluate
        evaluation = evaluate_strategy(strategy, profile)
        results.append(
            {
                "iteration": i,
                "strategy": strategy,
                "score": evaluation["score"],
                "total_wealth": evaluation["total_wealth"],
                "goal_achievement": evaluation["goal_achievement"],
            }
        )

        if evaluation["score"] > best_score:
            best_score = evaluation["score"]
            best_strategy = strategy

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


if __name__ == "__main__":
    # Example usage
    profile = generate_synthetic_profile()
    print("Financial Profile:")
    print(f"  Monthly Income: ${profile.monthly_income:.2f}")
    print(f"  Savings Goal: ${profile.savings_goal:.2f}/year")
    print()

    # Run optimization
    results = optimize_strategy(profile, iterations=5)

    print("Top Strategies:")
    for i, res in enumerate(results[:3]):
        print(f"\n{i + 1}. Score: {res['score']:.3f}")
        print(f"   Strategy: {json.dumps(res['strategy'], indent=2)}")
        print(f"   Total Wealth: ${res['total_wealth']:.2f}")
        print(f"   Goal Achievement: {res['goal_achievement']:.1%}")
