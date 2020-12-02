
import random


def main():
    score = float(input("Enter score: "))
    print(result(score))
    score = random.randint(0, 100)
    print(result(score))


def result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


main()