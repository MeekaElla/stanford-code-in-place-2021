from karel.stanfordkarel import *

"""
File: SafePickup.py
--------------------
When you finish writing this file, Karel should be able to
pick up a beeper from the current position if one is present
(but do nothing if no beepers are present).
"""


def main():
    """
    Karel can pick up beepers, but not if none are present!
    """
    if beepers_present():
        pick_beeper()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('SafePickup1.w')
