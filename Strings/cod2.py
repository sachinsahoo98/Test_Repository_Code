"""
WAP to show below prop

Input = ["abc12", "def", "ghi23", "kl"]
Output = ["abc", "def", "ghi", "kl"]
"""

def removeIntegers(lst):
    newList = []
    for string in lst:
        resultantString = ""
        for char in string:
            if not char.isdigit():
                resultantString+= char
        newList.append(resultantString)
    return newList

a = ["abc12", "def", "ghi23", "kl"]
result = removeIntegers(a)
print(result)