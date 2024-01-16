"""
-------------------------------------------------------
[Lab 2, Task 12]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-09-22"
-------------------------------------------------------
"""
# Constants
# TODO: defines the variable to label the number of seconds in one minute
SECONDS_PER_MINUTE = 60
# TODO: defines the variable to label the number of seconds in one hour 
SECONDS_PER_HOUR = 3600
# TODO: defines the variable to label the number of seconds in one day
SECONDS_PER_DAY = 86400

# Inputs
# TODO: asks the user to input the number of seconds
seconds = int(input("Number of seconds: "))

# Calculations
# TODO: calculates the number of seconds in a day
days = seconds // SECONDS_PER_DAY
# TODO: calculates the remainder of seconds
seconds %= SECONDS_PER_DAY

# TODO: calculates the number of seconds in a hour
hours = seconds // SECONDS_PER_HOUR
# TODO: calculates the remainder of seconds
seconds %= SECONDS_PER_HOUR

# TODO: calculates the number of seconds in a minute
minutes = seconds // SECONDS_PER_MINUTE
# TODO: calculates the remainder of seconds
seconds %= SECONDS_PER_MINUTE

# Outputs
print()
print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
