"""
-------------------------------------------------------
[Lab 2, Task 2]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""

# Constants
# TODO: define the freezing point in fahrenheit
FREEZING_POINT_FAHRENHEIT = 32

# Inputs
fahrenheit = int(input("Enter temperature in Fahrenheit to convert into Celsius: "))

# Calculations
# TODO: calculate converting fahrenheit to celsius
celsius = (fahrenheit - FREEZING_POINT_FAHRENHEIT) * 5/9

#Outputs
print("Temperature (F):", fahrenheit)
print("Temperature (C):", celsius)