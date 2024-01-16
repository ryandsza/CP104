"""
-------------------------------------------------------
Midterm A Task 4 Function Definitions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""


def result(response):
    """
    DO NOT CHANGE THE CONTENTS OF THIS FUNCTION
    -------------------------------------------------------
    Determines how a response should be classified.
    Use: classification = result(response)
    -------------------------------------------------------
    Parameters:
        response - a response to classify (str)
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        classification - the response classification (str)
    -------------------------------------------------------
    """
    if response == 'Win':
        classification = 'Epic!'
    elif response == 'Loss':
        classification = 'Brutal'
    else:
        classification = 'Say what?'
    return classification
