# Professional Python Calculator CLI

![Build Status](https://github.com/Reyesfrancisp/pro-calculator/actions/workflows/python-app.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)

A robust, modular command-line interface (CLI) calculator application built with Python. This project demonstrates professional software engineering practices, including design patterns (Factory, Facade), comprehensive testing (100% coverage), and continuous integration (GitHub Actions).

## Features

* **Hybrid REPL Interface:** Supports both fast one-line commands (`add 5 10`) and interactive guided inputs for better user experience.
* **Standard Operations:** Addition, Subtraction, Multiplication, and Division.
* **History Management:** Tracks all calculations in a session and displays them in a formatted, readable table.
* **Robust Error Handling:** Implements both "Look Before You Leap" (LBYL) and "Easier to Ask Forgiveness than Permission" (EAFP) strategies to manage invalid inputs and mathematical errors gracefully.
* **Modular Architecture:** Strictly separates logic (`operations`), data models (`calculation`), and state management (`calculator`) to adhere to the Single Responsibility Principle.
* **100% Test Coverage:** Verified using `pytest` and `pytest-cov`.

## Project Structure

```text
pro-calculator/
├── app/
│   ├── __init__.py
│   ├── calculation/    # Calculation class & Factory logic
│   ├── calculator/     # History state management (Facade)
│   └── operations/     # Pure math functions
├── tests/              # Pytest test suite
├── .github/            # GitHub Actions CI/CD workflows
├── main.py             # CLI Entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

## Setup Instructions

1. Clone the Repository

git clone [https://github.com/Reyesfrancisp/pro-calculator.git](https://github.com/Reyesfrancisp/pro-calculator.git)
cd pro-calculator

2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Windows:


python -m venv venv
source venv/Scripts/activate


Mac/Linux:


python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt
Usage
Start the calculator by running the main script:


python main.py


### Command Reference

| Command | Usage | Description |
| :--- | :--- | :--- |
| **add** | `add 5 10` | Adds two numbers. |
| **subtract** | `subtract 10 4` | Subtracts second number from first. |
| **multiply** | `multiply 6 7` | Multiplies two numbers. |
| **divide** | `divide 8 2` | Divides first number by second. |
| **history** | `history` | Shows a table of past calculations. |
| **help** | `help` | Displays the help menu. |
| **exit** | `exit` | Exits the application. |


Example Session

The application supports both Fast Mode (one line) and Guided Mode (step-by-step).


Calc> add 5 5
  = Result: 10

Calc> divide
  > Selected operation: divide
  > Enter first number: 10
  > Enter second number: 0
  ! Error: Cannot divide by zero.

Calc> history
  No.  | Operation  | Input A  | Input B  | Result
  -------------------------------------------------------
  1    | add        | 5        | 5        | 10
  2    | divide     | 10       | 0        | Error



Testing
This project enforces 100% test coverage. To run the tests and verify coverage locally:

# Run tests with coverage report
python -m pytest --cov=app --cov-report=term-missing
Continuous Integration
This repository uses GitHub Actions to automatically run tests on every push. The build will fail if test coverage drops below 100%.

Workflow config: .github/workflows/python-app.yml