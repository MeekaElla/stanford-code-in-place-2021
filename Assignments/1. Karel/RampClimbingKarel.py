from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def step_up():
    move()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()


def main():
    """
    Karel draw a diagonal line across the world, with a slope of ½
    """
    put_beeper()
    while front_is_clear():
        step_up()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
