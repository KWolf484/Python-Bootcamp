print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")

    age = int(input("What is your age? "))
    if age <= 12:
        print("Child ticket is $5.")
        bill = 5
    elif age <= 18:
        print("Youth ticket is $7.")
        bill = 7
    else:
        print("Adult ticket is $12.")
        bill = 12

    photo = input("Would you like a photo? (Y)es or (N)o").lower()
    if photo == "y" or photo == "yes":
        bill += 3
    print(f"Please pay {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

