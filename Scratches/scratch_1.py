### user turn ###
users_turn = True
while users_turn:
    if not bust_or_bj(player_score=user_score, player_hand=user_hand):
        print(f"Computers currently hand is {display(comp_hand)}")
        print(f"You currently have {display(user_hand)}\nScoring {user_score}")
        draw_card = input(f"Draw another card?\n(Y)es or (N)o: ").lower()
        if draw_card == "yes" or draw_card == "y":
            user_score = draw(player_hand=user_hand, num_cards=1)
            if bust_or_bj(player_hand=user_hand, player_score=user_score):
                print(f"You Bust with {user_score}\n************ You Lose! ************")
                cont_game = False
                return cont_game
        elif draw_card == "no" or draw_card == "n":
            users_turn = False
    elif bust_or_bj(player_hand=user_hand, player_score=user_score):
        has_ace(player_hand=user_hand, player_score=user_score)

### comp turn ###
comp_turn = True
while comp_turn:
    if comp_score < 17 and len(comp_hand) < 5 and bust_or_bj(player_hand=comp_hand, player_score=comp_score) == False:
        comp_score = draw(player_hand=comp_hand, num_cards=1)
        if bust_or_bj(player_hand=comp_hand, player_score=comp_score):
            print(f"Computer bust with {comp_hand}: {comp_score}")
            print(f"************ You Win! ************")

if user_score > comp_score:
    print(f"User score is:{user_score}\nComputer score is {comp_score}")
    print(f"************ You Win! ************")
    comp_turn = False
    cont_game = False
elif comp_score > user_score:
    print(f"Computer score is {comp_score}\nUser score is:{user_score}")
    print(f"************ You Lose! ************")
    comp_turn = False
    cont_game = False