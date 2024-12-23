"""
Write a Python program that matches a string that has an a followed by zero or more b's.
"""
import re

def checkString(charStr):
    match = re.search(r'^a*b*$', charStr)
    if match:
        return True
    return False

print(checkString('a'))

