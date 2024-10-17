

user_hand = [5, 7, 11]
user_score = 23


def bust_or_ace(player_hand, player_score):
    if player_score > 21:
        for card in player_hand:
            if card == 11:
                player_hand.remove(11)
                player_hand.append(1)
                return player_hand

        else:
            return player_hand


bust_or_ace(player_hand=user_hand,player_score=user_score)
print(user_hand)