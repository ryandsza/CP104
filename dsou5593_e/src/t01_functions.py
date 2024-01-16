"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    total = 0
    count = 0
    ea = 0
    
    for value in values:
        if value % 2 == 0:
            total += value
            count += 1
            
        if count == 0:
            ea = 0
        else:
            ea = total // count
            
    return ea
    
    
    
    
