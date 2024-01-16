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
from functions import student_stats

file_path = "students.txt"
with open(file_path, "r", encoding="utf-8") as file_handle:
    l_id, h_id, avg = student_stats(file_handle)

print(f"{l_id},{h_id},{avg}")



