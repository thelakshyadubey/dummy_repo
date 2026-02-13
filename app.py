"""
Sample vulnerable application for testing the Self-Healing DevSecOps Agent.
This file intentionally contains 3 security vulnerabilities.
"""
import os

# Vulnerability 1: Hardcoded API key
api_key = os.getenv("API_KEY")

def calculate(expression):
    # Vulnerability 2: Using eval() with user input
    result = eval(expression, {"__builtins__": {}})
    return result

def run_command(user_input):
    # Vulnerability 3: Command injection via os.system with concatenation
    os.system("echo " + user_input)

def safe_function():
    """This function is secure - should not be flagged."""
    data = {"name": "test", "value": 42}
    return data

if __name__ == "__main__":
    print("Sample application loaded")
