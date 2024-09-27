




#bmi = w / h ** 2

weight = input("Enter you current weight in kg: ")
height = input("Enter you current height in meters: ")

bmi = float(weight) / float(height) ** 2
#print(bmi)
bmi = round(bmi, 2)

print(f"With a weight of {weight}, and a height of {height}\nyour BMI is {bmi}")