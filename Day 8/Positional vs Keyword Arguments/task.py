# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")



def multi_input_greeting(name, age, location):
    print(f"Hi, my name is {name}\n"
          f"I'm from a place called {location}\n"
          f"and I am {age} years old")

multi_input_greeting(name="Derk", age="45", location="England")