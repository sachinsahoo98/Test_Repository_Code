"""
Given a String, perform uppercase of the later part of the string.

Input : test_str = 'geeksforgeek'
Output : geeksfORGEEK
Explanation : Latter half of string is uppercased.
"""

def convertUppercase(inputStr):
    length = len(inputStr)
    return inputStr[:length//2] + inputStr[length//2:].upper()


def UppercaseConvertWithoutSpaces(testStr):
    outStr = "".join(testStr.split())
    length = len(testStr)
    index = 0
    outputStr= ""
    for char in outStr:
        if index >= length//2:
            outputStr+=char.upper()
        else:
            outputStr += char
        index+=1
    return outputStr

def testFunction1():
    assert convertUppercase("geeksforgeek") == 'geeksfORGEEK'

def testFuncton2():
    assert UppercaseConvertWithoutSpaces("test only left") == 'testonlYLEFT'

