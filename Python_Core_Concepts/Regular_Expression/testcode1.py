"""
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
"""

import re

def checkString(charStr):
    match = re.search("[^a-zA-Z0-9]", charStr)
    if match:
        return False
    return True

def test_Validation():
    assert checkString("GeeksforGeeks") == True
    assert checkString("GFG123#") == False

