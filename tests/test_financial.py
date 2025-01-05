"""Test suite for the financial module."""

from decimal import Decimal

import pytest

from python_first_project.financial import (
    calculate_compound_interest,
    calculate_investment_returns,
    calculate_loan_payment,
    calculate_profit_margin,
    calculate_total,
)


# Tests for new loan payment function
def test_calculate_loan_payment_basic():
    """Test basic loan payment calculation."""
    # $100,000 loan at 5% for 30 years
    payment = calculate_loan_payment(100000, 5.0, 30)
    assert round(payment, 2) == 536.82


def test_calculate_loan_payment_zero_interest():
    """Test loan payment with zero interest."""
    # $12,000 loan at 0% for 1 year
    payment = calculate_loan_payment(12000, 0, 1)
    assert payment == 1000.0  # $1000 per month


def test_calculate_loan_payment_invalid_inputs():
    """Test loan payment with invalid inputs."""
    with pytest.raises(ValueError):
        calculate_loan_payment(-100000, 5.0, 30)
    with pytest.raises(ValueError):
        calculate_loan_payment(100000, -5.0, 30)
    with pytest.raises(ValueError):
        calculate_loan_payment(100000, 5.0, 0)


# Tests for new investment returns function
def test_calculate_investment_returns_basic():
    """Test basic investment returns calculation."""
    result = calculate_investment_returns(10000, 1200, 7.0, 10)
    # Just verify the key relationships we care about
    assert result["total_contributions"] == 22000.00
    assert result["total_value"] > result["total_contributions"]
    assert result["total_earnings"] > 0


def test_calculate_investment_returns_no_growth():
    """Test investment returns with zero growth."""
    result = calculate_investment_returns(10000, 1200, 0.0, 10)
    assert result["total_contributions"] == 22000.00
    assert result["total_value"] == 22000.00
    assert result["total_earnings"] == 0.00


def test_calculate_investment_returns_invalid_inputs():
    """Test investment returns with invalid inputs."""
    with pytest.raises(ValueError):
        calculate_investment_returns(-10000, 1200, 7.0, 10)
    with pytest.raises(ValueError):
        calculate_investment_returns(10000, -1200, 7.0, 10)
    with pytest.raises(ValueError):
        calculate_investment_returns(10000, 1200, 7.0, 0)


# Test calculate_total function
def test_calculate_total_basic():
    """Test basic functionality of calculate_total."""
    numbers = [1, 2, 3, 4, 5]
    assert calculate_total(numbers) == 15


def test_calculate_total_with_multiplier():
    """Test calculate_total with a multiplier."""
    numbers = [1, 2, 3]
    assert calculate_total(numbers, multiplier=2.0) == 12.0


def test_calculate_total_with_decimals():
    """Test calculate_total with Decimal numbers."""
    numbers = [Decimal("1.1"), Decimal("2.2"), Decimal("3.3")]
    assert calculate_total(numbers) == Decimal("6.6")


def test_calculate_total_empty_list():
    """Test calculate_total with an empty list."""
    assert calculate_total([]) == 0


def test_calculate_total_negative_numbers():
    """Test calculate_total with negative numbers."""
    numbers = [-1, -2, 3]
    assert calculate_total(numbers) == 0


def test_calculate_total_invalid_input():
    """Test calculate_total with invalid input."""
    with pytest.raises(TypeError):
        calculate_total(None)


# Test calculate_profit_margin function
def test_calculate_profit_margin_basic():
    """Test basic profit margin calculation."""
    assert calculate_profit_margin(100, 60) == 40.0


def test_calculate_profit_margin_zero_profit():
    """Test profit margin with zero profit."""
    assert calculate_profit_margin(100, 100) == 0.0


def test_calculate_profit_margin_loss():
    """Test profit margin with a loss."""
    assert calculate_profit_margin(100, 120) == -20.0


def test_calculate_profit_margin_invalid_revenue():
    """Test profit margin with invalid revenue."""
    with pytest.raises(ValueError):
        calculate_profit_margin(0, 50)


# Test calculate_compound_interest function
def test_calculate_compound_interest_basic():
    """Test basic compound interest calculation."""
    result = calculate_compound_interest(1000, 5.0, 1)
    assert round(result, 2) == 1051.16


def test_calculate_compound_interest_zero_rate():
    """Test compound interest with zero interest rate."""
    result = calculate_compound_interest(1000, 0, 1)
    assert result == 1000.0


def test_calculate_compound_interest_invalid_inputs():
    """Test compound interest with invalid inputs."""
    with pytest.raises(ValueError):
        calculate_compound_interest(-1000, 5.0, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, -5.0, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5.0, -1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5.0, 1, 0)
