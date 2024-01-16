"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-02"
-------------------------------------------------------
"""
# Imports
from random import randint

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0
    guess = 0

    while guess != number:
        guess = int(input("Guess: "))
        count += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")

    print(f"You made {count} guesses.")
    return count
    
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    total = 0
    num = 1

    while True:
        total += num ** 2
        if total >= target:
            return total
        num += 1

def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    negatives = 0
    zeroes = 0
    positives = 0

    num = float(input("First value: "))

    while num != -999:
        if num < 0:
            negatives += 1
        elif num == 0:
            zeroes += 1
        else:
            positives += 1
        num = float(input("Next value: "))

    return negatives, zeroes, positives

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0.0
    l_total = 0.0
    s_total = 0.0
    a_total = 0.0
    day = 1

    while True:
        print(f"For Day {day}\n")
        print()
        b_cost = float(input("How much was breakfast? $"))
        l_cost = float(input("How much was lunch? $"))
        s_cost = float(input("How much was supper? $"))

        day_total = b_cost + l_cost + s_cost
        print(f"Your total for the day was ${day_total:.2f}\n")

        b_total += b_cost
        l_total += l_cost
        s_total += s_cost
        a_total += day_total

        another_day = input("Were you away another day (Y/N)? ")
        if another_day.upper() != 'Y':
            break

        day += 1

    return b_total, l_total, s_total, a_total

def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the highest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    while True:
        value = int(input(f"Enter a value between {low} and {high}: "))
        if value < low:
            print("Value entered is too low")
        elif value > high:
            print("Value entered is too high")
        else:
            return value