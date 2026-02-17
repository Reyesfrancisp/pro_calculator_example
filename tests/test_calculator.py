import pytest
from app.calculator import Calculator
from app.calculation import Calculation
from app.operations import add, subtract

@pytest.fixture
def clear_history():
    """Fixture to clear history before each test."""
    Calculator.clear_history()

def test_add_calculation(clear_history):
    """Test adding a calculation to history."""
    calc = Calculation(2, 2, add)
    Calculator.add_history(calc)
    assert Calculator.get_latest() == calc

def test_get_history(clear_history):
    """Test retrieving the entire history."""
    calc1 = Calculation(2, 2, add)
    calc2 = Calculation(3, 3, subtract)
    Calculator.add_history(calc1)
    Calculator.add_history(calc2)
    assert Calculator.get_history() == [calc1, calc2]

def test_clear_history(clear_history):
    """Test clearing the history."""
    calc = Calculation(2, 2, add)
    Calculator.add_history(calc)
    Calculator.clear_history()
    assert Calculator.get_history() == []

def test_get_latest_empty(clear_history):
    """Test getting latest from empty history returns None."""
    assert Calculator.get_latest() is None