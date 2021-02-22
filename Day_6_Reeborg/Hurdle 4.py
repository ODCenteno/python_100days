def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if wall_in_front() and not wall_on_right():
        jump()
    elif wall_in_front():
        turn_left()
    elif not wall_on_right():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
