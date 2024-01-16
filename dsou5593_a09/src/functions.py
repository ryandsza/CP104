"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line_number = 0
    while line_number < count:
        line = file_handle.readline().strip()
        if not line:
            break
        print(line)
        line_number += 1

    return None

def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    number_list = []
    for line in file_handle:
        tokens = line.strip().split(',')
        for token in tokens:
            if token.isdigit() and int(token) > 0:
                number_list.append(int(token))
    return number_list
    
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    ucount = lcount = dcount = wcount = rcount = 0

    for line in file_handle:
        for char in line:
            if char.isupper():
                ucount += 1
            elif char.islower():
                lcount += 1
            elif char.isdigit():
                dcount += 1
            elif char.isspace():
                wcount += 1
            else:
                rcount += 1

    return ucount, lcount, dcount, wcount, rcount

def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line_number = 0
    for line in fh_read:
        fh_write.write(f"[{line_number}] {line}")
        line_number += 1

def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    total_marks = 0
    total_students = 0
    lowest_mark = float('inf')
    highest_mark = float('-inf')
    l_id = h_id = ""
    
    for line in file_handle:
        surname, forename, student_id, mark = line.strip().split(',')
        mark = int(mark)
    
        if mark < lowest_mark:
            lowest_mark = mark
            l_id = student_id
    
        if mark > highest_mark:
            highest_mark = mark
            h_id = student_id
    
        total_marks += mark
        total_students += 1

    if total_students > 0:
        avg = total_marks / total_students
    else:
        avg = 0.0
    
    return l_id, h_id, avg