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

def countMatching(str1, str2):

    initialDict = {}
    countOccurance = 0
    for char in str1:
        for character in str2:
            if character not in initialDict and character == char:
                countOccurance+=1
                initialDict[character] = 1
    print(initialDict)
    return countOccurance

print(countMatching("abcdef", "defghia"))
print(countMatching("aabcddekll12@", "bb2211@55k"))

