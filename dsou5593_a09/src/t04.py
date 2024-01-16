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
from functions import line_numbering

with open("wilde.txt", "r", encoding="utf-8") as fh_read:
    with open("wilde_numbered.txt", "w", encoding="utf-8") as fh_write:
        line_numbering(fh_read, fh_write)