"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""

def list_factors(number):
    """
    -------------------------------------------------------
    Returns a list of factors that make up the given number.
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - an integer greater than 0 (int)
    Returns:
        factors - a list of factors of the given number (int)
    -------------------------------------------------------
    """
    factors = [i for i in range(1, number) if number % i == 0]
    return factors

def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []

    while True:
        user_input = int(input("Enter a positive number: "))
        
        if user_input <= 0:
            break

        number_list += [user_input]

    return number_list

def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = [index for index in range(len(numbers)) if numbers[index] == target_number]
    return index_list

def find_indexes(values, target):
    indexes = [index for index in range(len(values)) if values[index] == target]
    return indexes

def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Returns a new list containing values from minuend that are
    not in subtrahend.
    Use: result = list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        result - a new list containing values from minuend not in subtrahend (list)
    ------------------------------------------------------
    """
    indexes_to_remove = find_indexes(minuend, subtrahend)
    
    for index in reversed(indexes_to_remove):
        minuend = minuend[:index] + minuend[index+1:]
    return None

def list_of_positives():
    number_list = []

    while True:
        user_input = int(input("Enter a positive number: "))
        
        if user_input <= 0:
            break

        number_list.append(user_input)

    return number_list

def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    if not numbers:
        result = True, -1

    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            result = False, index + 1

    result = True, -1
    
    return result
