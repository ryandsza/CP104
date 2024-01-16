"""
-------------------------------------------------------
Midterm A Task 2 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""


def categorize(points):
    """
    -------------------------------------------------------
    Determines the video game skill rating given win/lose/draw points.
        If points are 800 or greater, the rating is "Grandmaster".
        If points are 400 or greater but less than 800, the rating is "Master".
        If points are 200 or greater but less than 400, the rating is "Player".
        If points are 0 or greater but less than 200, the rating is "Noob".
        If points is less than 0, return "Error"
    Must use a fallthrough algorithm.
    Use: rating = categorize(points)
    -------------------------------------------------------
    Parameters:
        points - win/loss/draw points (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        category - description of skill rating (str)
    -------------------------------------------------------
    """

    if points >= 800:
        category = "Grandmaster"
    elif points >= 400:
        category = "Master"
    elif points >= 200:
        category = "Player"
    elif points >= 0:
        category = "Noob"
    else:
        category = "Error"

    return category
