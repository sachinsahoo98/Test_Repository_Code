"""
Python program to check if a string has at least one letter and one number

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""

#Sol1
def checkString(inpStr):

    countNum, countAlpha = 0, 0
    result = False
    if inpStr == "" or inpStr ==" ":
        return result
    else:
        for letter in inpStr:
            if letter.isdigit():
                countNum+=1
            elif letter.isalpha():
                countAlpha+=1
        if countAlpha >=1 and countNum>=1:
            result = True
    return result

listStrings = ["welcome2ourcountry34", "stringwithoutnum", " ", "n1"]
for string in listStrings:
    print(f"Checking At least \'{string}\' string has one letter and one number: {checkString(string)}")
