"""
-------------------------------------------------------
Midterm A Task 3 Function Definitions
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants
BASE_COST = 95.00
COST_PER_EXTRA_SERVICE = 35.00
VIP_DISCOUNT_RATE = 0.15


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a car cleaned. The cost is made up of:
        base cost: $95.00
        cost per extra service: $35.00
        VIP discount 15% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌‌‌‌​​​‌‌‌‌​​‌:
        cost - cost of cleaning a car based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    extra_services = int(input("How many extra services are you purchasing? "))
    is_vip = input("Are you a VIP member? (Y/N)? ")

    if is_vip == 'Y':
        if extra_services > 1:
            cost = BASE_COST + (extra_services * COST_PER_EXTRA_SERVICE) - (VIP_DISCOUNT_RATE * BASE_COST)
        else:
            cost = BASE_COST + (extra_services * COST_PER_EXTRA_SERVICE)
    else:
        cost = BASE_COST + (extra_services * COST_PER_EXTRA_SERVICE)

    return cost
