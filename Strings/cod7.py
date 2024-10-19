"""
WAP To check string is symmetrical or palindrome
"""

def checkPalindrome(inputStr):
    lengthStr = len(inputStr)
    for index in range(0, lengthStr//2):
        if inputStr[index] != inputStr[lengthStr-index-1]:
            return False
    return True

def checkSymmetrical(inputStr):
    size = len(inputStr)
    if size % 2 == 0:
        firstString = inputStr[0: size//2]
        lastString = inputStr[size//2 : size]
    else:
        firstString = inputStr[0: size//2]
        lastString = inputStr[size//2 + 1 : size]

    if firstString != lastString:
        return False
    return True

stringsToValidate = []
print("Enter User Strings:")
for value in range(3):
    string = input("")
    stringsToValidate.append(string)
print("User Provided Strings:", stringsToValidate)

#Display Result
for string in stringsToValidate:
    print("Checking for :", string)
    if checkPalindrome(string):
        print("String is palindrome")
    else:
        print("Not a Palindrome")
    if checkSymmetrical(string):
        print("String is Symmetrical")
    else:
        print("Not a Symmetrical")
