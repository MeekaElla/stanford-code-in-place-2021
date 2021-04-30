from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to pick up all beepers from the first row of any sized world.
"""


def main():
    """
    Karel will walk across the bottom row
    and at each position picking up a beeper
    only if one is present
    """
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Cleanup1.w')
