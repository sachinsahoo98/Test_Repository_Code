"""
Python program to count number of vowels using sets in given string.
Input : GeeksforGeeks
Output : No. of vowels : 5
Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.
"""

def countVowels(inputStr):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    countVowel = 0

    for char in inputStr:
        if char in vowels:
            countVowel+=1
    return countVowel


def cVowels(input):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in input if char in vowels)

print(countVowels("GeeksforGeeks"))
