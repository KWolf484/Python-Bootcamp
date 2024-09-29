import random
#imports ASCII art for RPS from ./art.py
from art import rock, paper, scissors

#Constatent variables
ROCK = 0
PAPER = 1
SCISSORS = 2
ascii_art = [rock, paper, scissors]
#Ask player to make a choice between RPS
player = input("Choose: (R)ock, (P)aper or (S)cissors.\n").upper()

#Assigns a random (0 1 2) integer to variable comp
comp = random.randint(0, 2)

"""Assigns player choice to corresponding number R=0 P=1 S=2"""
if player == "R" or player == "ROCK":
    player = ROCK
elif player == "P" or player == "PAPER":
    player = PAPER
elif player == "S" or player == "SCISSORS":
    player = SCISSORS
else:
    print("Player input wasn't recognized, try again")

def win_lose(p, c):
    """Take two args (p = player, c = comp) and evaluated who wins"""
    if p == c:
        print("Draw")
    elif p == 0 and c == 2 or p == 1 and c == 0 or p == 2 and c == 1:
        print("You Win")
    else:
        print("You Lose")

def ascii_art(x):
    """prints ASCII art using value of x (0, 1, 2) as index for list art"""
    return ascii_art[x]


print(f"Player:\n{ascii_art(x=player)}")
print(f"Computer:\n{ascii_art(x=comp)}")
win_lose(p=player, c=comp)
