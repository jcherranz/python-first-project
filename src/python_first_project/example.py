"""Example module demonstrating code quality best practices.

This module provides utility functions for numerical calculations
and demonstrates proper Python code organization.
"""

from typing import List, Optional


def calculate_total(numbers: List[int], multiplier: Optional[float] = None) -> float:
    """Calculate the total of a list of numbers, with optional multiplier.

    Args:
        numbers: List of numbers to sum
        multiplier: Optional value to multiply the sum by

    Returns:
        float: The calculated total
    """
    total = sum(numbers)
    if multiplier is not None:
        total *= multiplier
    return total


# Example usage
if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5]
    result = calculate_total(sample_numbers, 2.0)
    print(f"The total is: {result}")
