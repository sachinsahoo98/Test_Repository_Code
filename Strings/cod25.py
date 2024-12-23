import pytest

def reverseStrSol1(inputStr):
    return inputStr[::-1]

def reverseStrSol2(inpStr):
    revStr = ""
    if inpStr == "":
        return None
    strLen = len(inpStr)
    for index in range(strLen - 1, -1, -1):
        revStr += inpStr[index]

    return revStr

def test_reverseStrSol1():
    assert reverseStrSol1("Sachin") == "nihcaS"

def test_reverseStrSol2():
    assert reverseStrSol2("") == None