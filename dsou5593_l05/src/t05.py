"""
-------------------------------------------------------
[Lab 5, Task 5]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""
# Imports
from functions import is_leap

# Inputs
year = int(input("Enter the year to check whether it is a leap year or not: "))

# Calculations
result = is_leap(year)

# Outputs
print(f"The year {year} is: {result}")