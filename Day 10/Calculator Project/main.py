from art import logo
from os import system

def add(n1, n2):
    """Takes two arguments, adding and returns the result"""
    return n1 + n2

def subtract(n1, n2):
    """Take two arguments, subtracts n2 from n1 and returns result"""
    return n1 - n2

def multiply(n1, n2):
    """Takes two arguments, multiples n1 by n2 and returns the result"""
    return n1 * n2

def divide(n1, n2):
    """Takes two arguments and divides n1 by n2 and returns the result """
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    cont_with_last = True
    print(logo)
    num1 = int(input("First number: "))
    while cont_with_last:
        operator = input("Which operation: + - / *, ? ")
        num2 = int(input(f"Second number: "))
        result = operators[operator](n1=num1, n2=num2)
        print(f"{num1} {operator} {num2} = {result}")

        cont = input(f"(Y)es or (N)o;\nWould you like to continue working with {result}, or start a new calculation?").lower()
        if cont == "yes" or cont == "y":
            num1 = result
        else:
            result = 0
            cont_with_last = False
            system('clr')
            calculator()

calculator()


