"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("  5  " + str(round(per_min * 5, 1)))
    for i in range(10, minutes + 1, 5):
        calories_burned = round(per_min * i, 1)
        print(str(i) + "  " + str(calories_burned))

def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an arrow of # characters pointing up.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows for the arrow (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, rows + 1):
        if i == 1:
            print(" " * (rows - i) + "#")
        elif i == rows:
            print("#" + " " * (2 * i - 3) + "#")
        else:
            print(" " * (rows - i) + "#" + " " * (2 * i - 3) + "#")

def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"{'':>12}", end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:^6}", end="")
    print()
    print(f"{'':>12}{'-' * 18}")

    for i in range(start_num, stop_num + 1):
        print(f"{i:<10}|", end="")
        for j in range(start_num, stop_num + 1):
            print(f"{i * j:^6}", end="")
        print()

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for _ in range(count):
        total += start
        start += increment
    return total