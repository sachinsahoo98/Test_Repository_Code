"""
To check if string is palindrome or not

Generic Approach:
A string is said to be palindrome if it appears same from backward as well as forward also.

For example : naman, nitin, 123321, 451

1. Traverse the string, start comparing the elements from beginning to each element from the end, if they are not same
 return false else return true, its palindrome

"""
def checkPalindrome(inpString):
    if inpString == "":
        return None
    else:
        lenStr = len(inpString)
        for index in range(0, int(lenStr/2)):
            if inpString[index]!= inpString[lenStr-1-index]:
                return False
        return True

print(checkPalindrome("Rohit"))
print(checkPalindrome("naman"))


"""
Approach2: Split the string into two equal halves and check for the equality of first part with reversed last part
"""

def checkPalindrome(strInp):
    lengthSize = len(strInp)
    if lengthSize%2 == 0:
        firstPart = strInp[0: lengthSize//2]
        lastPart = strInp[lengthSize//2: lengthSize]
    else:
        firstPart = strInp[0: lengthSize // 2]
        lastPart = strInp[(lengthSize // 2)+1: lengthSize]

    if firstPart == lastPart[::-1]:
        return True
    else:
        return False

print(checkPalindrome("radar"))
print(checkPalindrome("nappy"))