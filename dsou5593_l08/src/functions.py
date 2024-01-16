"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-07"
-------------------------------------------------------
"""
# Imports 
from random import randint
 
name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    return (name[d - 1])

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = [randint(low, high) for i in range(n)]
    
    return values

def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = 0
    count = 0

    for value in values:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
        total += value
        count += 1

    average = total / count

    return smallest, largest, total, average

def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0

    for value in values:
        if value < 0:
            negatives += 1
        elif value > 0:
            positives += 1
        else:
            zeroes += 1

        if value % 2 == 0:
            evens += 1
        else:
            odds += 1

    return negatives, positives, zeroes, evens, odds

def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: product = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        product - source1 • source2 (float)
    -------------------------------------------------------
    """
    
    product = 0.0
    i = 0

    while i < len(source1):
        product += source1[i] * source2[i]
        i += 1

    return product

def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    
    target = [item for item in source1 if item not in source2] + [item for item in source2 if item not in source1]

    return target