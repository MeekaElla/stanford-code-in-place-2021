"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    print(f"What is {num1} + {num2}? ")
    total = num1 + num2
    user_answer = int(input("Your answer: "))
    if user_answer == total:
        print("Correct!")
    else:
        print(f"Incorrect. The expected answer is {total}")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
