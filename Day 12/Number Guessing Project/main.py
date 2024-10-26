from random import randint

WIN = "************ You Win ************"
LOSE = "************ You Lose ************"
GAME_OVER = "************ Game Over ************"
LOWER = "Guess Lower"
HIGHER = "Guess Higher"

num_to_guess = randint(1,101)


def game_mode():
    """
    Sets the game mode difficulty based on the users input
    :return: int(num)
    """
    print("Difficulty selection:\n(H)ard = 5 chances\n(E)asy = 10 chances.")
    difficulty = input("Please select either (H)ard or (E)asy: ").lower()
    num = 0
    if difficulty == "h" or difficulty == "hard":
        num = 5
    elif difficulty == "e" or difficulty == "easy":
        num = 10
    else:
        print("Selection not recognised, please try again. ")
        game_mode()

    return num

def higher_or_lower(guess, ans):
    """
    Determines if the users guess was equal too, lower or higher than the random number generated
    :param guess:
    :param ans:
    :return: LOWER, HIGHER or WIN
    """
    if guess > ans:
        return LOWER
    elif guess < ans:
        return HIGHER
    elif guess == ans:
        return WIN
    else:
        print("So wierd shite happen?! ")

def play_game():
    """
    Asks user if they want to play
    :return: function game() or ends script
    """
    print("Do you want to play a number guessing game?")
    play = input("(Y)es or (N)o: ").lower()
    if play == "y" or play == "yes":
        game()
    elif play == "n" or play == "no":
        print("Bye bye")

    else:
        print("Something went wrong!?")
        play_game()



def game():
    """
    Main game flow.
    :return: Variable = WIN, LOSE or GAME_OVER
    """
    game_over = False
    chances = game_mode()
    print(chances)
    guesses = []
    while chances > 0 and not game_over :
        print(f"Previous guesses: {guesses}\nNumber of chances left: {chances}")
        user_guess = int(input("Guess a number between 1 and 100: "))
        guesses.append(user_guess)
        current_turn = higher_or_lower(user_guess, num_to_guess)
        print(current_turn)

        if current_turn == WIN:
            game_over = True
        elif current_turn == LOWER:
            chances -= 1
        elif current_turn == HIGHER:
            chances -= 1
    else:
        if chances == 0:
            print(f"You ran out of chances\n{LOSE}\n{GAME_OVER}")
            play_game()
        elif game_over:
            print(GAME_OVER)
            play_game()

play_game()






























