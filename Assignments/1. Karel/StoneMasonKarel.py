from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        repair_damage()
    if front_is_blocked():
        last_repair()


def repair_damage():
    if no_beepers_present():
        put_beeper()
    turn_left()
    if front_is_blocked():
        turn_right()
        for i in range(4):
            move()
    else:
        while beepers_present():
            move()
        put_beeper()
        while front_is_clear():
            move()
            if no_beepers_present():
                put_beeper()
        face_south()
        go_back()
        for i in range (3):
            move()


def last_repair():
    if no_beepers_present():
        put_beeper()
    turn_left()
    if front_is_blocked():
        turn_right()
    else:
        if beepers_present():
            move()
        put_beeper()
        while front_is_clear():
            move()
            if no_beepers_present():
                put_beeper()
        face_south()
        while front_is_clear():
            move()
        turn_left()


def face_south():
    for i in range(2):
        turn_left()


def go_back():
    while beepers_present():
        move()
        if front_is_blocked():
            turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('SampleQuad1.w')
