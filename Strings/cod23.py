"""
Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

def changeString(sampleStr):
    firstChar = sampleStr[0]
    nextString = sampleStr[1:].replace(firstChar, "$")
    return firstChar + nextString


p = changeString("restart")
print(p)