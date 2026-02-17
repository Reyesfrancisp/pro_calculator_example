"""
Calculation and Factory Module.

This module defines the Calculation class, which represents a single mathematical
operation involving two operands (x and y) and a specific operation function.
It also includes the CalculationFactory, which implements the Factory design pattern
to instantiate Calculation objects based on string operation names.
"""

from app.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, x: float, y: float, operation: callable):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self) -> float:
        return self.operation(self.x, self.y)

    def __repr__(self):
        """Return a string representation of the calculation."""
        return f"Calculation({self.x}, {self.y}, {self.operation.__name__})"

class CalculationFactory:
    @staticmethod
    def create(x: float, y: float, operation: str) -> Calculation:
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        return Calculation(x, y, operations[operation])