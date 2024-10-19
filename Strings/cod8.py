"""
Reverse Words of a string in python

Input  : Hi this is sachin
Output : sachin is this Hi
"""

#Sol1
def reverseWords(inputstr):
    initList = inputstr.split(" ")
    rString = " ".join(reversed(initList))
    return rString

print(reverseWords("Hi this is sachin"))

#Sol2
def reverseWords(inputString):
    reverseString = []
    word = ""
    for char in inputString:
        if char != " ":
            word+=char
        else:
            reverseString.append(word)
            word = ""
    reverseString.append(word)
    return " ".join(reversed(reverseString))

print(reverseWords("Hi this is sachin"))
