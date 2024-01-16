"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Ryan D'souza
ID:     169065593
Email:  dsou5593@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports

from t07_functions import line_lengths

with open("source.txt", "r", encoding="utf-8") as fh_read:
    with open("source2.txt", "w", encoding="utf-8") as fh_write:
        line_lengths(fh_read, fh_write)
    with open("source3.txt", "r", encoding="utf-8") as fh_read:
        line_lengths(fh_read, None)
    