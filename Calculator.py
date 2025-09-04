# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 20:19:14 2025

@author: Mritunjoy Paul
"""

# Basic Calculator with Error Handling

# --- Calculator Functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

# --- Main Program ---
while True:
    print("\n--- Basic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "6":
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
        elif choice == "5":
            print("Result:", power(num1, num2))
        else:
            print("Invalid choice! Please select a valid option.")

    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError as e:
        print("Error:", e)
