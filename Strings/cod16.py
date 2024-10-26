"""
Given a sequence abcdef123456
print : a1b2c3d4e5f6
"""

def parseString(inputStr):
    length = len(inputStr)
    charStr = inputStr[0: length//2]
    numberStr = inputStr[length//2:]
    resultStr = ""
    minLength = min(len(charStr), len(numberStr))

    for index in range(minLength):
        resultStr += charStr[index] + numberStr[index]
    return resultStr

resultStr = parseString("abcdef123456")
print(resultStr)