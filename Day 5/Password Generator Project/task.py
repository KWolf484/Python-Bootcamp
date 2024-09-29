import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
#Asks user for amount of each character type to be used in generating the password
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

###Non-random order password generation###
#Takes user inputs and randomly chooses chars from corresponding lists,
#adding them to a string, prints string
password = ""
for item in range(1, nr_letters +1):
    password += random.choice(letters)
for item in range(1, nr_symbols +1):
    password += random.choice(symbols)
for item in range(1, nr_numbers +1):
    password += random.choice(numbers)
print(password)


###Randomises password char order###
#Transfers password into a list, and randomly shuffles the order
pass_list = []
for item in password:
    pass_list.append(item)
random.shuffle(pass_list)

#Transfers list items into a string, prints string
rand_password = ""
for item in pass_list:
    rand_password += item
print(rand_password)










