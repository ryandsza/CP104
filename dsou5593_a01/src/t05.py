"""
-------------------------------------------------------
[Assignment 1, Task 5]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""

# Inputs
principal = float(input("Principal: $"))
interest_percentage = float(input("Interest (%): ")) 
years = int(input("Number of years: "))
interest_compounded = int(input("Number of times interest compounded per year: "))

# Calculations
interest = interest_percentage / 100.0
amount = principal * (1 + interest / interest_compounded) ** (interest_compounded * years)

#Outputs
print("Balance: $", amount)