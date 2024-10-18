
user_hand = [10, 10, 11]



def calc_hand(player_hand):
    score = 0
    """
    Calc the given players hands, tests for blackjack(-1) OR returns the player_score
     
    :Example:
    >>>calc_hand(user_hand[10,8]
    18
    >>>calc_hand(10,11)
    -1
    """
    if len(player_hand) == 2 and sum(player_hand) == 21:
        return -1
    else:
        return sum(player_hand)


def bust(player_hand):
    if calc_hand(player_hand) > 21:
        if 11 in player_hand:
            player_hand.remove(11)
            player_hand.append(1)
    elif calc_hand(player_hand) <= 21:
        return False
    elif calc_hand(player_hand) > 21:
        return True






if calc_hand(user_hand) == -1:
    print(f"************ BLACKJACK ************\n************ YOU WIN ************\nWith hand {user_hand}")
elif bust(user_hand):
    user_score = calc_hand(player_hand=user_hand)
    print(f"Bust with {user_score}, with hand {user_hand}")
elif not bust(user_hand):
    user_score = calc_hand(player_hand=user_hand)
    print(f"************ YOU WIN ************\nScore: {user_score} Hand: {user_hand}")

