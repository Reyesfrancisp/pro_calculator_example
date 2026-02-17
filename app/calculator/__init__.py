"""
Calculator State and History Management Module.

This module defines the Calculator class, which acts as the core manager
for the application. It maintains a class-level history of all performed
calculations and provides static methods to add to, retrieve from, and 
clear this history log.
"""

from typing import List
from app.calculation import Calculation

class Calculator:
    history: List[Calculation] = []  # Class-level variable to store history

    @staticmethod
    def add_history(calculation: Calculation):
        """Adds a calculation to the history."""
        Calculator.history.append(calculation)

    @staticmethod
    def clear_history():
        """Clears the calculation history."""
        Calculator.history.clear()

    @staticmethod
    def get_last_calculation() -> Calculation:
        """Retrieves the last calculation from history."""
        if Calculator.history:
            return Calculator.history[-1]
        return None