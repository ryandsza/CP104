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
user_input = int(input("Enter a date in the format YYYYMMDD: "))

# Calculations
year = user_input // 10000
month_day = user_input % 10000
month = month_day // 100
day = month_day % 100

# Outputs
print()
print(f"The reformatted date: {year}/{month:02}/{day:02}")