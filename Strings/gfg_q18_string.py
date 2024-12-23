"""
Program to check if a string contains any special character
"""

import re

def checkSpecialChar(inputStr):

    specialChars = '~`!@#$%^&*(){}[]?/<>|'
    status = "Accepted"
    for char in inputStr:
        if char in specialChars:
            status = "Not Accepted"
    return status

print(checkSpecialChar("$GeeksFor$Geeks"))


def stringCheckTest(testStr):

    testSequence = re.compile('[`!@#%&$*(^)[]{}><?:/]')
    if testSequence.search(testStr) == None:
        return 0
    else:
        return 1

print(stringCheckTest("$GeeksFor$Geeks"))