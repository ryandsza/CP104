"""
-------------------------------------------------------
Midterm A Task 1 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants
TWENTIES = 20
TENS = 10
FIVES = 5
LOONIES = 1

def minimal_change(dollars):
    """
    -------------------------------------------------------
    Breaks down dollars into a minimal number of bills and coins.
    The change can be:
        twenties - bills worth 20 dollars
        tens - bills worth 10 dollars
        fives - bills worth 5 dollars
        loonies - coins worth 1 dollar
    Use: twenties, tens, fives, loonies = minimal_change(dollars)
    -------------------------------------------------------
    Parameters:
        dollars - number of dollars (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        twenties - number of $20 bills (int)
        tens - number of $10 bills (int)
        fives - number of $5 bills (int)
        loonies - number of $1 coins (int)
    -------------------------------------------------------
    """

    twenties = dollars // TWENTIES
    dollars %= TWENTIES
    tens = dollars // TENS
    dollars %= TENS
    fives = dollars // FIVES
    dollars %= FIVES
    loonies = dollars

    return twenties, tens, fives, loonies
