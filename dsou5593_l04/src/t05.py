"""
-------------------------------------------------------
[Lab 4, Task 5]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import right_triangle

# Inputs
# TODO: Asks the user to enter the length of the adjacent side
adjacent = float(input("Enter the length of the adjacent side: "))
# TODO: Asks the user to enter the length of the opposite side
opposite = float(input("Enter the length of the opposite side: "))

# Calculations
# TODO: Calculates the hypotenuse, perimeter, and area using the right_triangle function
hyp, per, area = right_triangle(adjacent, opposite)

# Outputs
print(f"({hyp}, {per}, {area})")