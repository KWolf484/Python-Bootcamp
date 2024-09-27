print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percent = (tip / 100) +1
subtotal = round(bill * percent)
total = round(subtotal / people, 2)

print(f"Bill total is {subtotal}\nThat will be {total} per person.")



