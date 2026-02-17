import pytest
from app.calculation import Calculation, CalculationFactory
from app.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (10, 5, add, 15),
    (10, 5, subtract, 5),
    (10, 5, multiply, 50),
    (10, 5, divide, 2),
])
def test_calculation_operations(a, b, operation, expected):
    """Test Calculation class with various operations."""
    calc = Calculation(a, b, operation)
    assert calc.get_result() == expected

def test_calculation_repr():
    """Test the string representation of the Calculation class."""
    calc = Calculation(10, 5, add)
    assert repr(calc) == "Calculation(10, 5, add)"

def test_divide_by_zero_exception():
    """Test division by zero in Calculation class."""
    calc = Calculation(10, 0, divide)
    with pytest.raises(ZeroDivisionError):
        calc.get_result()

def test_calculation_factory_add():
    """Test creating an addition calculation via Factory."""
    calc = CalculationFactory.create(10, 5, 'add')
    assert calc.get_result() == 15

def test_calculation_factory_invalid():
    """Test Factory with an invalid operation."""
    with pytest.raises(ValueError):
        CalculationFactory.create(10, 5, 'unknown')