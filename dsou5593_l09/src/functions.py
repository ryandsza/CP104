"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-17"
-------------------------------------------------------
"""

def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    
    no_digits = True
    no_upper_case = True
    no_lower_case = True

    for char in password:
        if char.isdigit():
            no_digits = False
        elif char.isupper():
            no_upper_case = False
        elif char.islower():
            no_lower_case = False

    if len(password) < 8:
        print("not long enough")

    if no_digits:
        print("no digits")

    if no_upper_case:
        print("no upper case")

    if no_lower_case:
        print("no lower case")
    return

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0
    vowels = "aeiouAEIOU"

    for char in s:
        if char in vowels:
            count += 1

    return count

def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    special_chars = "#@$%&!"

    count = 0
    for char in s:
        if char in special_chars:
            count += 1

    return count

def comma_period_replace(string):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        out - string with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = string.replace(',', '.')
    return out

def total_digits(string):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(string)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in string (int)
    ------------------------------------------------------
    """
    total = 0

    for char in string:
        if char.isdigit():
            total += int(char)

    return total