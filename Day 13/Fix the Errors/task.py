try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input, please use numerals such as 15.")

    age = int(input("How old are you?"))

    if age > 18:
        print(f"You can drive at age {age}.")
