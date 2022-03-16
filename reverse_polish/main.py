from art import logo
import sys


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)

    try:
        num1 = float(input("Enter Number ('x' to exit): "))
    except ValueError:
        sys.exit(1)

    is_on = True

    while is_on:

        try:
            num2 = float(input("Enter Another Number: "))
        except ValueError:
            sys.exit(1)

        symbol = input("Pick Operation: ")

        if symbol not in operations:
            return
        else:
            ans = operations.get(symbol)(num1, num2)

        print(f"{num1} {symbol} {num2} = {ans}")

        repondre = input("Continue? (Y/N): ").lower()

        if repondre.startswith("n"):
            is_on = False
            calculator()
        else:
            num1 = ans


if __name__ == "__main__":

    run_calc = input("Start Calculating? ").lower()
    if run_calc.startswith('y'):
        calculator()
    else:
        sys.exit(0)
