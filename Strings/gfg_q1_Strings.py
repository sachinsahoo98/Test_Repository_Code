"""
Python program to check whether the string is Symmetrical or Palindrome

Input: khokho
Output:
The entered string is symmetrical
The entered string is not palindrome

Input:amaama
Output:
The entered string is symmetrical
The entered string is palindrome

"""



def checkStringPalindrome(inpStr):
    """

    :param inpStr:
    :return: True if string is palindrome, False if not palindrome
    """
    strLen = len(inpStr)
    for index in range(int(strLen/2)):
        if inpStr[index]!= inpStr[strLen-1-index]:
            return False
    return True


def checkStringSymmetrical(testStr):
    strLength = len(testStr)
    firstPart = secondPart = None
    if strLength % 2==0:
        firstPart = testStr[:int(strLength/2)]
        secondPart = testStr[int(strLength/2):]
    else:
        firstPart = testStr[:int(strLength / 2)]
        secondPart = testStr[int(strLength / 2)+1:]

    if firstPart != secondPart:
        return False
    return True

def test_Check_Palindrome():
    assert checkStringPalindrome("NamaN") == True
    assert checkStringPalindrome("Mumma") == False

def test_Check_Symmetrical():
    assert checkStringSymmetrical("amaama") == True
    assert checkStringSymmetrical("mouni") == False