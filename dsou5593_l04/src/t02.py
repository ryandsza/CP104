"""
-------------------------------------------------------
[Lab 4, Task 2]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import circumference

# Inputs
# TODO: asks the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculations
# TODO: Calculates the circumference using the circumference function
circ = circumference(radius)

# Outputs
print(round(circ,2))