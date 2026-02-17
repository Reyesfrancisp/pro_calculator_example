import sys
from app.calculator import Calculator
from app.calculation import CalculationFactory

def repl():
    print("Professional Calculator CLI (Type 'exit' to quit, 'history' to see logs)")
    while True:
        user_input = input(">>> ").strip().lower()
        
        if user_input == 'exit':
            break
        if user_input == 'history':
            for idx, calc in enumerate(Calculator.history):
                print(f"{idx}: {calc.a} {calc.operation.__name__} {calc.b} = {calc.get_result()}")
            continue

        try:
            # Simple parser example: "add 5 10"
            parts = user_input.split()
            if len(parts) != 3:
                print("Usage: <operation> <num1> <num2>")
                continue
                
            op, n1, n2 = parts[0], float(parts[1]), float(parts[2])
            
            calc = CalculationFactory.create(n1, n2, op)
            result = calc.get_result()
            Calculator.add_calculation(calc)
            print(f"Result: {result}")
            
        except ZeroDivisionError:
            print("Error: Handled division by zero.")
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    repl()