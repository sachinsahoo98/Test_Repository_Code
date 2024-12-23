"""
Python program to capitalize the first and last character of each word in a string
Input: hello world
Output: HellO WorlD
Input: welcome to geeksforgeeks
Output: WelcomE TO GeeksforgeekS
"""

def capitalizeWordsinString(inputStr):
    words = inputStr.split()
    outputStr = ""
    for word in words:
        length = len(word)
        currentIndex = 0
        for char in word:
            if (currentIndex == 0 or currentIndex == length-1) and char.islower():
                outputStr+=char.upper()
            else:
                outputStr += char
            currentIndex+=1
        outputStr+=" "
    return outputStr.strip()


def testStrings():
    assert capitalizeWordsinString("hello world") == "HellO WorlD"