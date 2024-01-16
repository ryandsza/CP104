"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-10"
-------------------------------------------------------
"""

def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership. A member gets a
    discount according to the number of friends they sign up.
        0 friends: 0% discount
        1 friend: 5% discount
        2 friends: 10% discount
        3 or more friends: 15% discount
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    
    ONE_FRIEND_DISCOUNT = 0.05
    TWO_FRIENDS_DISCOUNT = 0.10
    THREE_OR_MORE_FRIENDS_DISCOUNT = 0.15
    
    if friends == 0:
        final_cost = cost
    elif friends == 1:
        final_cost = cost - (cost * ONE_FRIEND_DISCOUNT)
    elif friends == 2:
        final_cost = cost - (cost * TWO_FRIENDS_DISCOUNT)
    else:
        final_cost = cost - (cost * THREE_OR_MORE_FRIENDS_DISCOUNT)
        
    return final_cost

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        result = True
    else:
        result = False
    return result

def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    
    OVERTIME_RATE = 1.5
    TAX_RATE = 3.625 / 100

    if hours_worked > 40:
        regular_pay = 40 * hourly_rate
        OVERTIME_HOURS = (hours_worked - 40) * hourly_rate * OVERTIME_RATE
        gross_salary = regular_pay + OVERTIME_HOURS
    else:
        gross_salary = hours_worked * hourly_rate

    tax_amount = TAX_RATE * gross_salary
    net_payment = gross_salary - tax_amount

    return net_payment

def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    FULL_TIME_TEN_YEARS_RAISE = 0.05
    FULL_TIME_LESS_THAN_FOUR_YEARS_RAISE = 0.015
    PART_TIME_TEN_YEARS_RAISE = 0.03
    PART_TIME_LESS_THAN_FOUR_YEARS_RAISE = 0.01
    OTHER_RAISE = 0.02

    def pay_raise(status, years, salary):
        if status == 'F':
            if years >= 10:
                new_salary = salary * (1 + FULL_TIME_TEN_YEARS_RAISE)
            elif years < 4:
                new_salary = salary * (1 + FULL_TIME_LESS_THAN_FOUR_YEARS_RAISE)
            else:
                new_salary = salary * (1 + OTHER_RAISE)
        elif status == 'P':
            if years >= 10:
                new_salary = salary * (1 + PART_TIME_TEN_YEARS_RAISE)
            elif years < 4:
                new_salary = salary * (1 + PART_TIME_LESS_THAN_FOUR_YEARS_RAISE)
            else:
                new_salary = salary * (1 + OTHER_RAISE)
        else:
            new_salary = salary * (1 + OTHER_RAISE)
    
        return float(new_salary)

def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER_PRICE = 6.00
    WINGS_PRICE = 8.00
    FRIES_COMBO_PRICE = 1.50
    SALAD_COMBO_PRICE = 2.00

    print("Order B - burger or W - wings:")
    order = input()

    if order == 'B' or order == 'b':
        print("Make it a combo? (Y/N):")
        combo = input()
        if combo == 'Y' or combo == 'y':
            print("Add F - fries or S - salad:")
            side_order = input()
            if side_order == 'F' or side_order == 'f':
                price = BURGER_PRICE + FRIES_COMBO_PRICE
            elif side_order == 'S' or side_order == 's':
                price = BURGER_PRICE + SALAD_COMBO_PRICE
            else:
                price = BURGER_PRICE
        else:
            price = BURGER_PRICE
    elif order == 'W' or order == 'w':
        print("Make it a combo? (Y/N):")
        combo = input()
        if combo == 'Y' or combo == 'y':
            print("Add F - fries or S - salad:")
            side_order = input()
            if side_order == 'F' or side_order == 'f':
                price = WINGS_PRICE + FRIES_COMBO_PRICE
            elif side_order == 'S' or side_order == 's':
                price = WINGS_PRICE + SALAD_COMBO_PRICE
            else:
                price = WINGS_PRICE
        else:
            price = WINGS_PRICE
    else:
        price = 0.00

    return price