"""
Write a Python program to remove the nth index character from a nonempty string.

Example: input : sachin
Remove 3 index, output = sacin
"""

def removeCharatIndex(inputStr, position)-> str:
    """

    :param inputStr: takes input string
    :param position: takes index at index
    :return: output string with character removed from index position
    """

    resultStr = ""
    if len(inputStr) == 0:
        return resultStr
    else:
        for index in range(0, len(inputStr)):
            if index == position:
                continue
            else:
                resultStr+=inputStr[index]
    return resultStr

result = removeCharatIndex("sachin", 3)
print(result)