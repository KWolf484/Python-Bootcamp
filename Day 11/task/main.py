import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

comp_hand = []
user_hand = []

def draw(player_hand, num_cards):
    """Take two arguments, player name and number of cards to be drawn.
       passes players cards to calc_hand func """
    for card in range(num_cards):
        player_hand.append(random.choice(cards))
    return calc_hand(player_hand)

def calc_hand(player_hand):
    """Calc the given players hands, returns the hand_score """
    hand_score = 0
    for card in player_hand:
        hand_score += card
    return hand_score

def bust_or_bj(player_hand, player_score):
    """Check to see if player is bust (True),
    or has blackjack(-1)"""
    if len(player_hand) == 2 and player_score == 21:
        return -1 # f"{player} Drew {player[0]} and {player[1]},\n BLACK JACK!"
    else:
        if player_hand > 21:
            return True
        elif player_score <=21:
            return False

def has_ace(player_hand, player_score):
    if len(player_hand) > 2 and player_score > 21:
        return True
    else:
        return False

def display(player_hand):
    """take a list (player) """
    num_cards = len(player_hand)
    if player_hand == comp_hand and num_cards == 2:
        return f"{player_hand[0:num_cards - 1]} X"
    else:
        return f"{player_hand[0:num_cards]}"

def game():
    cont_game = True
    user_score = draw(player_hand=user_hand, num_cards=2)
    comp_score = draw(player_hand=comp_hand, num_cards=2)
    while cont_game:
        if bust_or_bj(user_hand, user_score) == -1:
            cont_game = False
            print(f"")

        if not bust_or_bj(comp_hand, comp_score) == -1:
            if bust_or_bj(comp_hand, comp_score):
                cont_game = False
                print(f"Computer bust with {comp_score}\n Player wins")

            while comp_score < 17 and len(comp_hand) < 5 and bust_or_bj(comp_hand, comp_score) != True:
                draw(comp_hand, comp_score)
                bust_or_bj(comp_hand, comp_score)
            else:
                if not bust_or_bj(comp_hand, comp_score):
                    cont_game = False



    else:
        return





    print(display(comp_hand))
    print(display(user_hand))
game()


