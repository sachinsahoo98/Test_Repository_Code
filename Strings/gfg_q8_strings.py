"""
Python program to check if a string has at least one letter and one number

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""

def checkString(string):
    numLetter = numDigit = 0
    result = False
    for char in string:
        if char.isdigit():
            numDigit+=1
        elif char.isalpha():
            numLetter+=1
        if numDigit>=1 and numLetter>=1:
            result = True
    return result

def testString():
    assert checkString("welcome2ourcountry34") == True
    assert checkString("stringwithoutnum") == False

