"""
Python | Count the Number of matching characters in a pair of string
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb2211@55k'
Output : 5
(i.e. matching characters :- b, 1, 2, @, k)
"""

def countMatchingPairs(str1, str2):

    outDict = {}
    countOccurance = 0
    for char in str1:
        for character in str2:
            if character not in outDict and character == char:
                countOccurance+=1
                outDict[character] = 1
    return countOccurance

def testValidation():

    assert countMatchingPairs("hlloew", "wellcome") == 4