"""
Calculator Command Line Interface (CLI) Entry Point.

This module provides a Read-Eval-Print Loop (REPL) for the calculator application.
It continuously prompts the user for arithmetic operations, parses the input,
and uses the CalculationFactory to execute the commands.
"""

import sys
from app.calculator import Calculator
from app.calculation import CalculationFactory

def repl():
    print("Welcome to the Professional Calculator. Type 'exit' to quit.")
    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == 'exit':
            break
            
        parts = user_input.split()
        if len(parts) != 3:
            print("Usage: <operation> <x> <y>")
            continue

        operation, x_str, y_str = parts

        # LBYL (Look Before You Leap): Check if operation exists before trying
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print(f"Error: Unknown operation '{operation}'")
            continue

        # EAFP (Easier to Ask Forgiveness): Try to convert numbers, catch the error if it fails
        try:
            x, y = float(x_str), float(y_str)
            # ... call your factory here ...
        except ValueError:
            print(f"Error: Invalid numbers. '{x_str}' or '{y_str}' is not a valid number.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

if __name__ == "__main__":  # pragma: no cover
    repl()