"""
-------------------------------------------------------
[Lab 4, Task 9]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import fraction_product

# Inputs
# TODO: Asks the user to enter the numerator of the first fraction
num1 = int(input("Enter the numerator of the first fraction: "))
# TODO: Asks the user to enter the denominator of the first fraction
den1 = int(input("Enter the denominator of the first fraction: "))
# TODO: Asks the user to enter the numerator of the second fraction
num2 = int(input("Enter the numerator of the second fraction: "))
# TODO: Asks the user to enter the denominator of the second fraction
den2 = int(input("Enter the denominator of the second fraction: "))

# Calculations
# TODO: Calculates the numerator, denominator and product using the fraction_product function
num, den, product = fraction_product(num1, den1, num2, den2)

# Outputs
print(f"({num}, {den}, {product})")