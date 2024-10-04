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

n1 = int(input("Enter first number: "))
func = operators[input("Choose from: +, -, *, /\nEnter an operator: ")]
n2 = int(input("Enter second number: "))
carry_result = 0
print(func(n1, n2))


