"""
Write a Python program that matches a string that has an a followed by three 'b'

"""
import re

def checkString(charStr):
    match = re.search(r'^ab{3}?', charStr)
    if match:
        return True
    return False

print(checkString('abbb'))
print(checkString('abbbbb'))
print(checkString('aaaabbb'))
print(checkString('aa'))
print(checkString('abbbaabbb'))
print("------------------------")


"""
Write a Python program that matches a string that has an a followed by two to three 'b''
"""

import re

def checkString(charStr):
    match = re.search(r'^ab{2,3}?', charStr)
    if match:
        return True
    return False

print(checkString('abbb'))
print(checkString('abbbbb'))
print(checkString('aaaabbb'))
print(checkString('aa'))
print(checkString('abbabbb'))
print(checkString('abbbaabbb'))
