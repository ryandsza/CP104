"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""

def customer_best(fh):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    result = []
    
    max_balance = float('-infinity')

    for line in fh:
        customer_data = line.strip().split(',')
        balance = float(customer_data[3])

        if balance > max_balance:
            max_balance = balance
            result = customer_data

    return result

def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    fields = [str(field) for field in fields]

    for field in fields[:-1]:
        fh.write(field + ',')
    fh.write(fields[-1] + '\n')
    return

def append_increment(fh):
    """
    -------------------------------------------------------
    Appends a number to the end of the fh. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    data = fh.readlines()
    new_data = []

    for num in data:
        new_data.append(int(num.strip()))

    highest = new_data[-1]
    fh.write(f"\n{highest + 1}")

    return (highest + 1)

def find_shortest(fh):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fh.
    Assumes file is not empty.
    Use: word = find_shortest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the first word with the shortest length in fh (str)
    ------------------------------------------------------
    """
    data = fh.readlines()
    length = float('infinity')
    shortest_word = ""

    for word in data:
        if len(word.strip()) < length:
            length = len(word.strip())
            shortest_word = word.strip()

    return shortest_word

def file_copy_n(fh_1, fh_2, n):
    """
    -------------------------------------------------------
    Copies n record from fh_1 (starting from the beginning of the file) to fh2
    Use: file_copy_n(fh_1, fh_2, n)
    -------------------------------------------------------
    Parameters:
        fh_1 - file to search (file handle - already open for reading)
        fh_2 - file to search (file handle - already open for appending)
        n - number of lines to copy from fh_1 to fh_2
    Returns:
        None
    ------------------------------------------------------
    """
    data = fh_1.readlines()

    number = int(n)

    while True:

        if (len(data) > number):
            for i in range(number):
                fh_2.write(data[i])
            break
        else:
            for i in range(len(data)):
                fh_2.write(data[i])
            number -= len(data)
            break
    return