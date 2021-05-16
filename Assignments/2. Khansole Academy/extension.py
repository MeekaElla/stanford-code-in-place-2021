"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


import random

NUM_CORRECT = 3


def main():
    counter = 0

    while counter < NUM_CORRECT:
        num1 = random.randint(10,99)
        num2 = random.randint(10,99)
        print(f"What is {num1} + {num2}? ")
        total = num1 + num2
        user_answer = int(input("Your answer: "))
        if user_answer == total:
            counter += 1
            print(f"Correct! You've gotten {counter} correct in a row")
        else:
            print(f"Incorrect. The expected answer is {total}")
            counter = 0
    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
