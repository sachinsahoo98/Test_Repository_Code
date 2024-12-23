"""Reverse Words in a Given String in Python

Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks
Input : str = "my name is laxmi"
output : str= laxmi is name my
"""

def reverseWordsString(testStr):
    testList = testStr.split()
    return " ".join(word for word in reversed(testList))

def test_reverseWords():
    assert reverseWordsString("my name is sachin") == "sachin is name my"