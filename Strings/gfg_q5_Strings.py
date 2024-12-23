"""
Input : test_str = ‘geeksforgeeks 33 best’
Output : 19
Explanation : Total characters are 19.


Input : test_str = ‘geeksforgeeks best’
Output : 17
Explanation : Total characters are 17 except spaces.
"""

def avoidSpaces(inputStr):
    totalCount = 0
    for char in inputStr:
        if char == " ":
            continue
        totalCount+=1
    return totalCount

def avoidSpacesList(inputStr):
    wordsList = inputStr.split()
    outputStr = "".join(word for word in wordsList)
    return len(outputStr)


def test_String():
    assert avoidSpaces('geeksforgeeks 33 best') == 19
    assert avoidSpaces('geeksforgeeks best') == 17
    assert avoidSpaces('')== 0

def test_String2():
    assert avoidSpacesList('hi this is sachin') == 14