"""
Calculation and Factory Module.

This module defines the Calculation class, which represents a single mathematical
operation involving two operands (x and y) and a specific operation function.
It also includes the CalculationFactory, which implements the Factory design pattern
to instantiate Calculation objects based on string operation names.
"""

from typing import Callable
from app.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, x: float, y: float, operation: Callable[[float, float], float]):
        self.x = x
        self.y = y
        self.operation = operation

    def get_result(self) -> float:
        # Calls the stored operation (e.g., add) using x and y
        return self.operation(self.x, self.y)

class CalculationFactory:
    @staticmethod
    def create(x: float, y: float, op_name: str) -> Calculation:
        # Dictionary mapping string names
        operations = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
        
        if op_name not in operations:
            raise ValueError(f"Unknown operation: {op_name}")
            
        return Calculation(x, y, operations[op_name])