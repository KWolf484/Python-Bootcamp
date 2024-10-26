import random
comp_hand = []
user_hand = []

def draw(player_hand, num_cards):
    """
    Take two arguments, player name and number of cards to be drawn.
    passes players cards to calc_hand func
    # :Example:
    # >>>draw(user_hand, 2)
    # user_hand = [9, 3]
    # user_score = calc_hand(user_hand)
    # 12
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for card in range(num_cards):
        player_hand.append(random.choice(cards))
    return calc_hand(player_hand)

def calc_hand(player_hand):
    """
    Calculates the given players hands, tests for blackjack;-1 OR returns the player_score
    # :Example:
    # >>>calc_hand(10, 8)
    # 18
    # >>>calc_hand(10, 11)
    # -1
    """
    if len(player_hand) == 2 and sum(player_hand) == 21:
        return -1
    else:
        return sum(player_hand)

def bust(player_hand):
    """
    Checks to see if a given hand;list is over 21;bust.
    If bust,check for Ace;11 is in the hand, and change to 1
    If still bust; returns True, if not bust; return False
    # :Example:
    # >>>bust(10, 5, 11)
    # 10, 5, 1
    # False
    # >>>bust(10, 3, 9)
    # 10, 3, 9
    # True
    """
    if calc_hand(player_hand) > 21:
        if 11 in player_hand:
            player_hand.remove(11)
            player_hand.append(1)
            player_score = calc_hand(player_hand)
            return player_score
    if calc_hand(player_hand) <= 21:
        return False
    if calc_hand(player_hand) > 21:
        return True

def bj_check():
    if calc_hand(comp_hand) == -1:
        print("Computer has Blackjack\n************ You lose *************")
        return True
    elif calc_hand(user_hand) == -1:
        print("Player has Blackjack\n************ You Win ************")
        return True
    else:
        return False


def display(player_hand):
    """
    takes a list (player)
    """
    num_cards = len(player_hand)
    if player_hand == comp_hand and num_cards == 2:
        return f"{player_hand[0:-1]}"
    else:
        return f"{player_hand[0:num_cards]}"

def compare(user_score, comp_score):
    scores = f"User score is: {user_score}; {user_hand}\nComputer score is: {comp_score}; {comp_hand}"
    if user_score == comp_score:
        print(f"{scores}\n ************ Draw ************")
    elif user_score > comp_score:
        print(f"{scores}\n************ You win ************")
    elif user_score < comp_score:
        print(f"{scores}\n************ You Lose ************")
    else:
        print("SOMETHINGS WHEN WRONG")



### Main game flow ###
def game():
    cont_game = True
    while cont_game:
    ### START ###
        user_score = draw(player_hand=user_hand, num_cards=2)
        comp_score = draw(player_hand=comp_hand, num_cards=2)
        bj_check()
        if bj_check():
            cont_game = False
        else:
            print("Current scores and cards,")
            print(f"Player score: {user_score} Hand: {display(user_hand).strip("")}")
            print(f"Computer score: XX Hand: {display(comp_hand).strip("]")}, X]")
    ### USER TURN ###
            user_cont = True
            while user_cont:
                bust(player_hand=user_hand)
                user_score = calc_hand(user_hand)
                if not bust(user_hand):
                    print("Players Turn.")
                    print(f"Player score: {user_score} Hand: {display(user_hand).strip("[]")}")
                    user_draw = input("Do you want to (H)it or (S)tick? ").lower()
                    if user_draw == "h" or user_draw == "hit":
                        user_score = draw(player_hand=user_hand,num_cards=1)
                        print(user_hand, user_score)
                    elif user_draw == "s" or user_draw == "stick":
                        print(user_hand, user_score)
                        user_cont = False
                elif bust(user_hand):
                    print(f"You drew card {user_hand[-1]} giving you a score of {user_score} busting ")
                    print("************ You Lose ************")
                    user_cont = False
                    cont_game = False
                    return cont_game, user_cont
        ### COMP TURN ###
            else:
                while calc_hand(comp_hand) < 17:
                    print(comp_hand)
                    if not bust(comp_hand):
                        draw(player_hand=comp_hand, num_cards=1)
                        comp_score = calc_hand(comp_hand)
                        print(f"Computer drew card: {comp_hand[-1]}")
                else:
                    if bust(comp_hand):
                        print(f"Computer drew card: {comp_hand[-1]}\nGiving them a score of {comp_score} busting ")
                        print("************ You Win ************")
                        cont_game = False
                    else:
                        compare(user_score, comp_score)
                        cont_game = False
game_over = False
while not game_over:
    play = input("Play Blackjack?\n(Y)es or (N)o: ").lower()
    if play == "y" or play == "yes":
        user_hand = []
        comp_hand = []
        game()
    elif play == "n" or play == "no":
        print("Thanks for playing")
        game_over = True


