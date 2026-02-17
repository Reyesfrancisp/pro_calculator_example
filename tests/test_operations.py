"""
Unit and Parameterized Tests for Operations.

This test suite verifies the correctness of the arithmetic operations
defined in app.operations. It utilizes pytest parameterization to efficiently
test a wide range of positive, negative, and edge-case inputs, including
exception handling for division by zero.
"""

import pytest
from app.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, 2),
    (5, -2, 3),
    (0, 0, 0),
    (10.5, 0.5, 11.0),
    (-1.5, -1.5, -3.0)
])
def test_add(x, y, expected):
    """Test addition with various integers and floats."""
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 2, 3),
    (1, 1, 0),
    (0, 5, -5),
    (10.5, 0.5, 10.0)
])
def test_subtract(x, y, expected):
    """Test subtraction with various scenarios."""
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (3, 3, 9),
    (-1, 5, -5),
    (0, 10, 0),
    (2.5, 2, 5.0)
])
def test_multiply(x, y, expected):
    """Test multiplication with various scenarios."""
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 5),
    (5, 2, 2.5),
    (0, 5, 0),
    (-10, 2, -5)
])
def test_divide(x, y, expected):
    """Test standard division."""
    assert divide(x, y) == expected

def test_divide_by_zero():
    """Test the division by zero exception (EAFP)."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)