"""
Python Program to remove all duplicates from a given string.
input : geeksforgeeks
Output : geksfor
"""

def clearDups(inputStr):
    outputStr = ""
    for char in inputStr:
        if char not in outputStr:
            outputStr+=char
    return outputStr

def tryRemovedups(inputVal):
    out = "".join(sorted(set(inputVal), reverse=True))
    return out

def testValidation():
    assert clearDups("geeksforgeeks") == 'geksfor'

def testVerify():
    assert tryRemovedups("niain") == 'nia'