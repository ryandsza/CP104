"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-10-28"
-------------------------------------------------------
"""

def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        return "Sunday"
    elif day_num == 2:
        return "Monday"
    elif day_num == 3:
        return "Tuesday"
    elif day_num == 4:
        return "Wednesday"
    elif day_num == 5:
        return "Thursday"
    elif day_num == 6:
        return "Friday"
    elif day_num == 7:
        return "Saturday"
    else:
        return "Error"
    
def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index < 0:
        return "Error"
    elif air_quality_index <= 50:
        return "Good"
    elif air_quality_index <= 100:
        return "Moderate"
    elif air_quality_index <= 150:
        return "Unhealthy for Sensitive Groups"
    elif air_quality_index <= 200:
        return "Unhealthy"
    elif air_quality_index <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"
    
def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    largest = max(val1, val2, val3)
    
    if val1 != largest:
        second_largest = max(val1, val2)
    elif val2 != largest:
        second_largest = max(val2, val3)
    else:
        second_largest = max(val1,val3)
        
        
    average = (largest + second_largest) / 2
    return average

def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if rgb_colour1 not in {"red", "green", "blue"} or rgb_colour2 not in {"red", "green", "blue"}:
        result = "Error"

    if rgb_colour1 == "red" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "red":
        result = "fuchsia"
    elif rgb_colour1 == "red" and rgb_colour2 == "green" or rgb_colour1 == "green" and rgb_colour2 == "red":
        result = "yellow"
    elif rgb_colour1 == "green" and rgb_colour2 == "blue" or rgb_colour1 == "blue" and rgb_colour2 == "green":
        result = "aqua"
    elif rgb_colour1 == rgb_colour2:
        result = rgb_colour1

    return result

def hoo_rah(number):
    """
    -------------------------------------------------------
    Returns a string based on the rules:
    - "Hoo" if the number is evenly divisible by 2
    - "Rah" if the number is evenly divisible by 7
    - "Hoo Rah" if the number is evenly divisible by both 2 and 7
    - "Zip" if the number is none of the above
    Use: hoo_rah(number)
    -------------------------------------------------------
    Parameters:
        number (int): The number inputted
    Returns:
        result (str): The string based on the divisibility rules
    -------------------------------------------------------
    """
    if number % 2 == 0 and number % 7 == 0:
        result = "Hoo Rah"
    elif number % 2 == 0:
        result = "Hoo"
    elif number % 7 == 0:
        result = "Rah"
    else:
        result = "Zip"
    return result