"""
Arithmetic Operations Module.

This module provides pure functions for basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""

def add(x: float, y: float) -> float:
    """Returns the sum of x and y."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Returns the difference of x and y."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Returns the product of x and y."""
    return x * y

def divide(x: float, y: float) -> float:
    """Returns the quotient of x and y. Raises ValueError on division by zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y