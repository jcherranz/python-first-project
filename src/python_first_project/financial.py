"""Financial calculations module.

This module provides functions for common financial calculations and analysis.
Includes tools for investment analysis, loan calculations, and basic financial metrics.
"""

from decimal import Decimal
from typing import Dict, List, Optional, Union

Number = Union[int, float, Decimal]


def calculate_loan_payment(principal: Number, annual_rate: float, years: int) -> float:
    """Calculate monthly payment for a loan.

    Args:
        principal: Loan amount
        annual_rate: Annual interest rate as percentage (e.g., 5.0 for 5%)
        years: Loan term in years

    Returns:
        Monthly payment amount

    Raises:
        ValueError: If any input values are negative or invalid
    """
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if years <= 0:
        raise ValueError("Years must be positive")

    monthly_rate = annual_rate / 1200  # Convert to monthly decimal rate
    num_payments = years * 12

    if monthly_rate == 0:
        return float(principal) / num_payments

    return float(principal * monthly_rate * (1 + monthly_rate) ** num_payments) / (
        (1 + monthly_rate) ** num_payments - 1
    )


def calculate_investment_returns(
    principal: Number, annual_contribution: Number, annual_rate: float, years: int
) -> Dict[str, float]:
    """Calculate investment growth with regular contributions.

    Args:
        principal: Initial investment amount
        annual_contribution: Yearly additional investment
        annual_rate: Expected annual return rate as percentage
        years: Investment timeframe in years

    Returns:
        Dictionary containing:
            - total_value: Final investment value
            - total_contributions: Sum of all contributions
            - total_earnings: Investment earnings

    Raises:
        ValueError: If any input values are invalid
    """
    if principal < 0 or annual_contribution < 0:
        raise ValueError("Investment amounts cannot be negative")
    if years <= 0:
        raise ValueError("Years must be positive")

    rate_decimal = annual_rate / 100
    total_value = float(principal)

    # Calculate growth year by year
    for _ in range(years):
        # Add contribution at start of year
        total_value += float(annual_contribution)
        # Apply growth
        total_value *= 1 + rate_decimal

    total_value = round(total_value, 2)
    total_contributions = round(
        float(principal) + (float(annual_contribution) * years), 2
    )

    return {
        "total_value": total_value,
        "total_contributions": total_contributions,
        "total_earnings": round(total_value - total_contributions, 2),
    }


# Keep existing functions
def calculate_total(
    numbers: List[Number], multiplier: Optional[float] = None
) -> Number:
    """Calculate the total of a list of numbers, with optional multiplier."""
    if numbers is None:
        raise TypeError("Numbers list cannot be None")

    total = sum(numbers)

    if multiplier is not None:
        if multiplier < 0:
            raise ValueError("Multiplier cannot be negative")
        total *= multiplier

    return total


def calculate_profit_margin(revenue: Number, costs: Number) -> float:
    """Calculate the profit margin as a percentage."""
    if revenue <= 0:
        raise ValueError("Revenue must be greater than zero")

    profit = revenue - costs
    return (profit / revenue) * 100


def calculate_compound_interest(
    principal: Number, rate: float, years: int, compounds_per_year: int = 12
) -> float:
    """Calculate compound interest over time."""
    if principal < 0:
        raise ValueError("Principal cannot be negative")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if years < 0:
        raise ValueError("Years cannot be negative")
    if compounds_per_year < 1:
        raise ValueError("Must compound at least once per year")

    rate_decimal = rate / 100
    return float(
        principal
        * (1 + rate_decimal / compounds_per_year) ** (compounds_per_year * years)
    )
