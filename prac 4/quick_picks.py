"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many number you picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number!")
        number_of_quick_picks = int(input("How many number you picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = []
        for o in range(NUMBERS_PER_LINE):
            numbers = random.randint(MIN, MAX)
            while numbers in quick_pick:
                numbers = random.randint(MIN, MAX)
            quick_pick.append(numbers)
        quick_pick.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()