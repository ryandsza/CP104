"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Inputs
num = int(input("Enter a positive two-digit number: "))

# Calculations
isolate_digit = num // 10
extract_digit = num % 10
difference = isolate_digit - extract_digit

# Outputs
print(f"The difference of the digits of {num} is {difference}")