"""
Program to print even letter words in a string

Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am
"""

#Sol1

def printEvenLettersWord(cstr):
    word = ""
    countChar = 0
    dictInit = {}

    for char in cstr:
        if char !=" ":
            word+=char
            countChar+=1
        else:
            dictInit[countChar]=word
            countChar = 0
            word= ""
    if countChar != 0:
        dictInit[countChar] = word
    for keyValue in dictInit.keys():
        if keyValue %2 == 0:
            print(str(dictInit[keyValue])+" ", end="")

printEvenLettersWord("This is a python language")
print("\n")

#Sol2

def printEvenLetters(charStr):
    Listnew = charStr.split()
    for item in Listnew:
        if len(item) % 2 == 0:
            print(item+" ", end="")

printEvenLetters("I am laxmi")