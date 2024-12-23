"""
Find words which are greater than given length k.
"""


def findWords(userStr, sizeK):
    outputList = []
    wordList = userStr.split()
    for word in wordList:
        if len(word) > sizeK:
            outputList.append(word)
    return " ".join(outputList)

print(findWords("Hi this is sachin", 4))

