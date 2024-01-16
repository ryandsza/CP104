"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Constants
dry_days = 0
damp_days = 0
wet_days = 0
avg = 0

def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """
    
    for i in range(0, 100000000000):
        rainfall = int(input("Rainfall mm (-1 to stop): "))
        
        if rainfall == -1:
            break
        
        if rainfall < 4:
            global dry_days
            dry_days += 1
        elif rainfall >= 4 and rainfall <= 8:
            global damp_days
            damp_days += 1
        else:
            global wet_days
            wet_days += 1
    
    avg = (dry_days + damp_days + wet_days) // 3
    
    return dry_days, damp_days, wet_days, avg
