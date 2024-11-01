"""
Least frequent char in a string

The original string is : GeeksforGeeks
The minimum of all characters in GeeksforGeeks is : f

"""

#Sol1
"""
charSeencount
"""


def findLeastFrequentChar(strInput):

    dictAlpha = {}
    for char in strInput:
        if char not in dictAlpha:
            dictAlpha[char] = 1
        else:
            dictAlpha[char] += 1
            
    return min(dictAlpha, key=dictAlpha.get)

print(findLeastFrequentChar("GeeksforGeeks"))