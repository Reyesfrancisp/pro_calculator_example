"""
Calculator State and History Management Module.

This module defines the Calculator class, which acts as the core manager
for the application. It maintains a class-level history of all performed
calculations and provides static methods to add to, retrieve from, and 
clear this history log.
"""

from app.calculation import Calculation
from typing import List

from app.calculation import Calculation
from typing import List

class Calculator:
    history: List[Calculation] = []

    @staticmethod
    def add_history(calculation: Calculation):
        """Add a calculation to the history."""
        Calculator.history.append(calculation)

    @staticmethod
    def clear_history():
        """Clear the calculation history."""
        Calculator.history.clear()

    @staticmethod
    def get_history() -> List[Calculation]:
        """Retrieve the full history."""
        return Calculator.history

    @staticmethod
    def get_latest() -> Calculation:
        """Retrieve the most recent calculation, or None if empty."""
        if Calculator.history:
            return Calculator.history[-1]
        return None