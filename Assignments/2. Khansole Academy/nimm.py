"""
File: nimm.py
-------------------------
Add your comments here.
"""

import random


def main():
    counter = 20
    player = 0
    while counter > 0:
        print(f"There are {counter} stones left")
        if player == 0:
            stones = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while stones == 0 or stones > 2:
                stones = int(input("Please enter 1 or 2: "))
            print("")
            player = 1
        else:
            stones = int(input("Player 2 would you like to remove 1 or 2 stones? "))
            while stones == 0 or stones > 2:
                stones = int(input("Please enter 1 or 2: "))
            player = 0
            print("")
        counter = counter - stones

    if player == 0:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
