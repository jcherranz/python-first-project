"""Test suite for the example module.

This module contains test cases for the example.py module's functionality,
demonstrating proper testing practices including:
- Test organization
- Edge cases
- Parameter validation
- Coverage considerations
"""

import pytest

from python_first_project.example import calculate_total


def test_calculate_total_basic():
    """Test basic functionality of calculate_total."""
    numbers = [1, 2, 3, 4, 5]
    assert calculate_total(numbers) == 15


def test_calculate_total_with_multiplier():
    """Test calculate_total with a multiplier."""
    numbers = [1, 2, 3]
    assert calculate_total(numbers, multiplier=2.0) == 12.0


def test_calculate_total_empty_list():
    """Test calculate_total with an empty list."""
    assert calculate_total([]) == 0


def test_calculate_total_negative_numbers():
    """Test calculate_total with negative numbers."""
    numbers = [-1, -2, 3]
    assert calculate_total(numbers) == 0


@pytest.mark.parametrize(
    "numbers, multiplier, expected",
    [
        ([1, 2, 3], 2.0, 12.0),
        ([0], 1.0, 0.0),
        ([-1, 1], -1.0, 0.0),
        ([10], 0.5, 5.0),
    ],
)
def test_calculate_total_parametrized(numbers, multiplier, expected):
    """Test calculate_total with various inputs using parametrize."""
    assert calculate_total(numbers, multiplier) == expected


def test_calculate_total_invalid_input():
    """Test calculate_total with invalid input."""
    with pytest.raises(TypeError):
        calculate_total(None)
