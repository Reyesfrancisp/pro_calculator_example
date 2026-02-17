"""
Calculator Command Line Interface (CLI) Entry Point.

This module provides a Read-Eval-Print Loop (REPL) for the calculator application.
It continuously prompts the user for arithmetic operations, parses the input,
and uses the CalculationFactory to execute the commands.
"""

import sys
from app.calculator import Calculator
from app.calculation import CalculationFactory

def display_menu():
    """Displays the available commands and usage instructions."""
    print("\n--- Professional Calculator ---")
    print("Usage: <operation> <x> <y>")
    print("Example: add 5 10")
    print("\nAvailable Operations:")
    print("  - add, subtract, multiply, divide")
    print("\nSpecial Commands:")
    print("  - history : View calculation history")
    print("  - help    : Show this menu")
    print("  - exit    : Quit the application")
    print("-------------------------------")

def repl():
    """Run the Read-Eval-Print Loop (REPL)."""
    # Show instructions only once at the start
    display_menu()

    while True:
        try:
            # distinct prompt to separate input from output
            user_input = input("\nCalc> ").strip().lower()
        except EOFError:
            break

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]

        # --- 1. Handle System Commands ---
        if command == 'exit':
            print("Goodbye!")
            break
        
        elif command == 'help':
            display_menu()
            continue

        elif command == 'history':
            history = Calculator.history
            if not history:
                print("  History is empty.")
            else:
                print(f"\n  {'No.':<4} | {'Operation':<10} | {'Input A':<10} | {'Input B':<10} | {'Result':<10}")
                print("-" * 55)
                for i, calc in enumerate(history, 1):
                    # Check if the calculation object has a stored result, or calculate it on the fly
                    res = calc.get_result()
                    print(f"  {i:<4} | {calc.operation.__name__:<10} | {calc.x:<10g} | {calc.y:<10g} | {res:<10g}")
            continue

        # --- 2. Handle Math Operations ---
        if command in ['add', 'subtract', 'multiply', 'divide']:
            
            x_str, y_str = None, None

            # Path A: Fast Mode (User typed "add 5 5")
            if len(parts) == 3:
                x_str, y_str = parts[1], parts[2]
            
            # Path B: Guided Mode (User typed just "add")
            elif len(parts) == 1:
                print(f"  > Selected operation: {command}")
                try:
                    x_str = input("  > Enter first number: ").strip()
                    y_str = input("  > Enter second number: ").strip()
                except ValueError:
                    print("  ! Error: Invalid input.")
                    continue
            else:
                print("Error: Invalid format. Try 'add 5 5' or just 'add'.")
                continue

            # --- 3. Execute Calculation ---
            try:
                # Convert inputs
                x = float(x_str)
                y = float(y_str)

                # Create and execute
                calc = CalculationFactory.create(x, y, command)
                result = calc.get_result()
                
                # Save to history
                Calculator.add_history(calc)

                # Display Result
                print(f"  = Result: {result:g}")

            except ValueError:
                print(f"  ! Error: Invalid numbers entered ('{x_str}', '{y_str}').")
            except ZeroDivisionError:
                print("  ! Error: Cannot divide by zero.")
            except Exception as e:
                print(f"  ! Error: {e}")

        else:
            # --- 4. Handle Unknown Commands ---
            print(f"Unknown command: '{command}'. Type 'help' for a list of commands.")

if __name__ == "__main__": # pragma: no cover
    repl()