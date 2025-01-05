Usage Guide
===========

Basic Usage
-----------

The main functionality is provided through the ``financial`` module:

.. code-block:: python

    from python_first_project.financial import calculate_total

    # Basic summation
    numbers = [100, 200, 300]
    total = calculate_total(numbers)
    print(f"Basic total: {total}")  # Output: 600

    # Using a multiplier
    total_with_markup = calculate_total(numbers, multiplier=1.2)
    print(f"Total with 20% markup: {total_with_markup}")  # Output: 720

Error Handling
--------------

The module includes proper error handling:

.. code-block:: python

    # TypeError for None input
    try:
        calculate_total(None)
    except TypeError as e:
        print(f"Error: {e}")  # Output: Error: Numbers list cannot be None

    # ValueError for negative multiplier
    try:
        calculate_total([100], multiplier=-1)
    except ValueError as e:
        print(f"Error: {e}")  # Output: Error: Multiplier cannot be negative

Type Hints
----------

The module supports type hints and works with different numeric types:

.. code-block:: python

    from decimal import Decimal

    # Using different number types
    mixed_numbers = [
        100,            # int
        200.5,         # float
        Decimal('300')  # Decimal
    ]

    total = calculate_total(mixed_numbers)
    print(f"Mixed types total: {total}")

Best Practices
--------------

1. Use appropriate numeric types for your calculations
2. Handle exceptions appropriately in your code
3. Consider using Decimal for financial calculations when precision is critical
4. Always validate input data before processing
