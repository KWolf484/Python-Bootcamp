# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")



def multi_input_greeting(name, age, location):
    print(f"Hi, my name is {name}\nI'm from {location}\nand I am {age} years old")

multi_input_greeting(name="Derk", age="45", location="England")