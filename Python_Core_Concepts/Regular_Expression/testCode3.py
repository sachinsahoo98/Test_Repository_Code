"""
 Write a Python program that matches a string that has an a followed by zero or one 'b'.
"""
import re

def checkString(charStr):
    match = re.search(r'^a*(b?)$', charStr)
    if match:
        return True
    return False

print(checkString('a'))
print(checkString('baaab'))
print(checkString('ab'))
print(checkString('aaaab'))
print(checkString('aaaa'))