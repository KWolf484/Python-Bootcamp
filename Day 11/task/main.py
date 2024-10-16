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
### Blackjack check, hand of 2 cards that sum to 21 ###
    if len(player_hand) == 2 and player_score == 21:
        return -1
### Bust check, hand sum over 21 ###
    elif player_score > 21:
        return True #BUST
    elif player_score <=21:
        return False

def has_ace(player_hand, player_score):
    bust = bust_or_bj(player_hand, player_score)
    if bust:
        player_hand.remove(11)
        player_hand.append(1)

    else:
        return player_hand

def display(player_hand):
    """takes a list (player) """
    num_cards = len(player_hand)
    if player_hand == comp_hand and num_cards == 2:
        return f"{player_hand[0:num_cards - 1]} X"
    else:
        return f"{player_hand[0:num_cards]}"



### Main game flow ###
def game():
    cont_game = True
    user_score = draw(player_hand=user_hand, num_cards=2)
    comp_score = draw(player_hand=comp_hand, num_cards=2)
    while cont_game:
        if bust_or_bj(comp_hand, comp_score) == -1:
            cont_game = False
            print(f"{comp_score}Computer has Blackjack!!\n************ You Lose! ************")
        elif bust_or_bj(user_hand, user_score) == -1:
            cont_game = False
            print(f"{user_score}BlackJack!!\n************ You Win! ************")



game()


