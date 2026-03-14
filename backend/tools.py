from typing import Optional, List, Dict, Any
import json
from datetime import datetime, timedelta
import random


def add_transaction(
    type: str,
    amount: float,
    category: str,
    date: Optional[str] = None,
    description: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Add a financial transaction to the user's records.

    Args:
        type: Type of transaction (income or expense)
        amount: Monetary amount (positive for income, negative for expense)
        category: Category of transaction (e.g., Food, Utilities, Income)
        date: Date of transaction in YYYY-MM-DD format (defaults to today)
        description: Description of the transaction

    Returns:
        dict: Confirmation with transaction ID
    """
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    # Generate a random transaction ID
    transaction_id = f"txn_{random.randint(1000, 9999)}"

    # In a real app, this would save to database
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "message": f"Transaction added: {description or category} for ${amount:.2f}",
        "timestamp": datetime.now().isoformat(),
    }


def get_budget_summary(period: str = "monthly") -> Dict[str, Any]:
    """
    Get budget summary for a specific period.

    Args:
        period: Time period (weekly, monthly, yearly)

    Returns:
        dict: Budget summary with income, expenses, savings
    """
    # Mock data - in real app, this would query database
    multiplier = {"weekly": 0.25, "monthly": 1, "yearly": 12}.get(period, 1)

    return {
        "period": period,
        "income": 5200 * multiplier,
        "expenses": 3850 * multiplier,
        "savings": 1350 * multiplier,
        "savings_rate": 26.0,
        "top_categories": [
            {"name": "Housing", "amount": 1200 * multiplier, "percentage": 31.2},
            {"name": "Food", "amount": 600 * multiplier, "percentage": 15.6},
            {"name": "Transportation", "amount": 400 * multiplier, "percentage": 10.4},
        ],
    }


def get_upcoming_bills() -> List[Dict[str, Any]]:
    """
    Get list of upcoming bills and their due dates.

    Returns:
        list: Upcoming bills with amounts and due dates
    """
    today = datetime.now()

    return [
        {
            "id": "bill_1",
            "name": "Rent",
            "amount": 1200.00,
            "due_date": (today + timedelta(days=11)).strftime("%Y-%m-%d"),
            "recurring": True,
            "category": "Housing",
        },
        {
            "id": "bill_2",
            "name": "Internet",
            "amount": 60.00,
            "due_date": (today + timedelta(days=6)).strftime("%Y-%m-%d"),
            "recurring": True,
            "category": "Utilities",
        },
        {
            "id": "bill_3",
            "name": "Insurance",
            "amount": 150.00,
            "due_date": (today + timedelta(days=14)).strftime("%Y-%m-%d"),
            "recurring": True,
            "category": "Insurance",
        },
    ]


def set_saving_goal(
    name: str,
    target_amount: float,
    deadline: Optional[str] = None,
    monthly_contribution: Optional[float] = None,
) -> Dict[str, Any]:
    """
    Set a new savings goal.

    Args:
        name: Name of the savings goal
        target_amount: Target amount to save
        deadline: Deadline date in YYYY-MM-DD format (optional)
        monthly_contribution: Monthly contribution amount (optional)

    Returns:
        dict: Confirmation with goal ID
    """
    goal_id = f"goal_{random.randint(1000, 9999)}"

    # Calculate required monthly contribution if deadline provided
    required_monthly = None
    if deadline and not monthly_contribution:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
        months = max(
            1,
            (deadline_date.year - datetime.now().year) * 12
            + (deadline_date.month - datetime.now().month),
        )
        required_monthly = target_amount / months

    return {
        "status": "success",
        "goal_id": goal_id,
        "message": f"Savings goal '{name}' created with target ${target_amount:.2f}",
        "required_monthly_contribution": required_monthly,
        "timestamp": datetime.now().isoformat(),
    }


def get_spending_analysis(
    period: str = "monthly", category: Optional[str] = None
) -> Dict[str, Any]:
    """
    Analyze spending patterns.

    Args:
        period: Time period to analyze
        category: Specific category to analyze (optional)

    Returns:
        dict: Spending analysis with insights
    """
    # Mock analysis data
    insights = [
        "You spend 30% more on weekends compared to weekdays.",
        "Your grocery spending has decreased by 15% this month.",
        "Dining out expenses are higher than average.",
        "Utility bills are consistent with previous months.",
    ]

    if category:
        insights = [i for i in insights if category.lower() in i.lower()]

    return {
        "period": period,
        "total_spending": 3850.00,
        "average_daily": 128.33,
        "comparison_to_last_period": -2.5,
        "insights": insights,
        "recommendations": [
            "Consider meal planning to reduce food expenses.",
            "Review subscription services for potential savings.",
            "Set up automatic transfers to your savings account.",
        ],
    }


def mock_investment_advice(beliefs: str = "moderate") -> Dict[str, Any]:
    """
    Get mock investment advice based on user beliefs/risk tolerance.

    Args:
        beliefs: Risk tolerance (conservative, moderate, aggressive)

    Returns:
        dict: Investment advice and mock portfolio
    """
    advice = {
        "conservative": {
            "allocation": {"stocks": 30, "bonds": 60, "cash": 10},
            "advice": "Focus on capital preservation with government bonds and high-yield savings.",
            "expected_return": "4-5% annually",
        },
        "moderate": {
            "allocation": {"stocks": 60, "bonds": 30, "cash": 10},
            "advice": "Balance between growth and stability with diversified index funds.",
            "expected_return": "6-7% annually",
        },
        "aggressive": {
            "allocation": {"stocks": 80, "bonds": 15, "cash": 5},
            "advice": "Focus on growth with high-growth stocks and emerging markets.",
            "expected_return": "8-10% annually",
        },
    }

    selected = advice.get(beliefs, advice["moderate"])

    return {
        "risk_profile": beliefs,
        "recommended_allocation": selected["allocation"],
        "advice": selected["advice"],
        "expected_return": selected["expected_return"],
        "mock_portfolio": {
            "total_value": 10000.00,
            "stocks": 10000 * selected["allocation"]["stocks"] / 100,
            "bonds": 10000 * selected["allocation"]["bonds"] / 100,
            "cash": 10000 * selected["allocation"]["cash"] / 100,
        },
    }


def generate_invoice(
    customer_name: str, items: List[Dict[str, Any]], due_days: int = 30
) -> Dict[str, Any]:
    """
    Generate a simple invoice.

    Args:
        customer_name: Name of the customer
        items: List of items with name, quantity, price
        due_days: Days until due date

    Returns:
        dict: Invoice details
    """
    invoice_id = f"INV-{random.randint(1000, 9999)}"
    subtotal = sum(item["quantity"] * item["price"] for item in items)
    tax = subtotal * 0.1  # 10% tax
    total = subtotal + tax

    due_date = (datetime.now() + timedelta(days=due_days)).strftime("%Y-%m-%d")

    return {
        "invoice_id": invoice_id,
        "customer": customer_name,
        "items": items,
        "subtotal": subtotal,
        "tax": tax,
        "total": total,
        "due_date": due_date,
        "status": "draft",
        "created_at": datetime.now().isoformat(),
    }
