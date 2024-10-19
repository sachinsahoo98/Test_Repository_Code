#WAP to remove duplicate elements from a string

"""
Input = "television"
Output = "tlvson"
"""

#Solution 1
def removeDuplicates(inputStr):
    rString = ""
    length = len(inputStr)
    for value in range(length):
        if inputStr[value] not in rString:
            rString+= inputStr[value]
    return rString

result = removeDuplicates("television")
print(result)

#Solution 2
def rmDups(inpStr):
    newStr = ""
    for char in newStr:
        if char not in newStr:
            newStr+= char
    return newStr

resultOutput = removeDuplicates("television")
print(resultOutput)
