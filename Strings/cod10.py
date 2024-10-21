"""
Input : test_str = 'geeksforgeek'
Output : geeksfORGEEK
Explanation : Latter half of string is uppercased.

Input : test_str = 'apples'
Output : appLES
Explanation : Latter half of string is uppercased.
"""
from operator import length_hint

"""
Approach: 
1. Use loop to iterate through the strings
2. If index is small than half of the actual length :
    store the value as it is
3. else uppercase the letter and store

"""


#Sol1
def convertUppercase(inputStr):

    size = len(inputStr)
    outputStr = ""
    indexValue = 0
    while(indexValue <= size-1):
        if indexValue >= int(size/2):
            outputStr+= inputStr[indexValue].upper()
        else:
            outputStr+= inputStr[indexValue]
        indexValue+=1

    return outputStr

result = convertUppercase("geeksforgeek")
result2 = convertUppercase("apples")
print(result, result2)

#Sol2

def convertUppercase(inputStr):

    outputStr = ""
    charScanned = 0
    strLen = len(inputStr)
    for char in inputStr:
        charScanned+=1
        if charScanned <= int(strLen/2):
            outputStr+= char
        else:
            outputStr += char.upper()
    return outputStr

result = convertUppercase("geeksforgeek")
result2 = convertUppercase("apples")
print(result, result2)

#Sol3
"""
Approach : 
Slice the entire strings into two equal halves.
first part will be stored as it is.
second part will be stored with uppercase letter.
"""

def testUppercase(inputStr):

    size = len(inputStr)
    return inputStr[:int(size/2)] + inputStr[int(size/2):].upper()

result = testUppercase("geeksforgeek")
result2 = testUppercase("apples")
print(result, result2)