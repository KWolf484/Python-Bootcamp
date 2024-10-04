import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

comp = []
user = []

def draw(player, num_cards):
    """Take two arguments, player name and number of cards to be drawn.
       passes players cards to calc_hand func """
    for card in range(num_cards):
    ### adds the given number of cards to the given player ###
        player.append(random.choice(cards))
    ### returns given players hand to the calc_hand func, ###
    ### which will calc and store hands current value     ###
    return calc_hand(player)

def calc_hand(player):
    """Calc the given players hands, returns the hand_score """
    hand_score = 0
### Iterates through players cards ###
    for card in player:
    ### adds each cards value to hand_score's total ###
        hand_score += card
    ### returns hand_score
    return hand_score

def is_bust(player, player_score):
    """Check to see if player is bust,
    and if player is holding an Ace """
    if len(player) > 2 and player_score > 21:
        for card in player:
            if card == 11:
                card = 1
            else:
                return True
            return player
    elif len(player) == 2 and player_score == 21:
        return f"{player} Drew {player[0]} and {player[1]},\n BLACK JACK!"


user_score = draw(player=user, num_cards=2)
comp_score = draw(player=comp, num_cards=2)

# user_Score = calc_hand(player=user)
# comp_score = calc_hand(player=comp)

print(f"User:{user} Score:{user_score}")
print(f"User:{comp} Score:{comp_score}")

