from art import logo

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move = input("(L)eft or (R)ight? ").capitalize()
if move == "L" or move == "Left":
    move = input("(S)wim or (W)ait? ").capitalize()
    if move == "W" or move == "Wait":
        print("There are three doors, (R)ed, (Y)ellow and (B)lue")
        move = input("Which one will you open? ").capitalize()
        if move == "Y" or move == "YELLOW":
            print("You Win!!")
        elif move == "R" or move == "RED":
            print("You're burned by fire,\nGame Over!!")
        elif move == "B" or move == "BLUE":
            print("You're eaten by a beast,\nGame Over!!")
        else:
            print("Game Over!!")
    else:
        print("Game Over!!")
else:
    print("Game Over!!")