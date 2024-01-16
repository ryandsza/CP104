"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    altered = ""
    
    for char in string:
        if char.lower() in "aeiou":
            altered += char.upper()
        else:
            altered += char.lower()
        
    return altered
