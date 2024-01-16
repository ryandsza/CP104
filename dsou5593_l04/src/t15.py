"""
-------------------------------------------------------
[Lab 4, Task 15]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import time_split

# Inputs
# TODO: Asks the user to enter the number of seconds
initial_seconds = int(input("Enter the number of seconds: "))

# Calculations
# TODO: Calculates the days, hours, minutes and seconds using the time_split function
days, hours, minutes, seconds = time_split(initial_seconds)

# Outputs
print(f"({days}, {hours}, {minutes}, {seconds})")