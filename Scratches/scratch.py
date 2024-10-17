def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    if wall_on_right():
        move()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()


while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        jump()