#Approach
"""
1. split the inputString across space to generate a list containing words
2. iterate through all the words and add reverse of each word to the outputString
3. return the word
"""

def reverseChars(inputStr):
    resultantString = ""
    inputList = inputStr.split()
    for word in inputList:
        resultantString += word[::-1] + " "
    return resultantString.strip()

resultOutput = reverseChars("my name is abhay")
print(resultOutput)