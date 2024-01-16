"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ryan D'Souza
ID: 169065593
Email: dsou5593@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports
from functions import valid_isbn

result1 = valid_isbn('978-3-12148410--0')
result2 = valid_isbn('978-3-16-148410-0')
result3 = valid_isbn('978-3-18-167494-0')

print(result1)
print(result2)
print(result3)