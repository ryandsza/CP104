"""
-------------------------------------------------------
Midterm A Task 1 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
from t01_functions import minimal_change

dollars = int(input("Dollars: "))
twenties, tens, fives, loonies = minimal_change(dollars)
print(f"minimal_change({dollars}) -> ({twenties}, {tens}, {fives}, {loonies})")
