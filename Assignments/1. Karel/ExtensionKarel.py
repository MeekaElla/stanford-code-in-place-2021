from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""


def main():
    turn_left()
    while front_is_clear():
        paint_corner(RED)
        move()
    turn_right()
    go_down()
    go_up()
    turn_right()
    while front_is_clear():
        move()
        paint_corner(RED)
    turn_left()


def go_up():
    move()
    turn_left()
    move()
    paint_corner(RED)
    move()
    turn_right()
    move()
    paint_corner(RED)


def go_down():
    paint_corner(RED)
    move()
    turn_right()
    move()
    paint_corner(RED)
    turn_left()
    move()
    turn_right()
    move()
    paint_corner(RED)
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
