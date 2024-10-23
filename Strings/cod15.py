"""

Given a string, count the number of vowels present in the given string using Sets. You can use sets to count the number
of vowels in a given string in Python. Sets are useful to efficiently check for counting
the unique occurrences of vowels.

Input : GeeksforGeeks
Output : No. of vowels : 5
Explaination: The string GeeksforGeeks contains 5 vowels in it 4 letter of 'e' and 1 'o'.
"""

#Sol1
def findVowels(inputStr):

    vowels = ['a', 'e', 'i', 'o', 'u']
    totalCountVowels = 0
    dictVowels = {}

    for char in inputStr.lower():
        if char in vowels:
            totalCountVowels+= 1
            if char not in dictVowels:
                dictVowels[char] = 1
            else:
                dictVowels[char]+= 1
    print(dictVowels)
    return totalCountVowels

numVowels = findVowels("GeeksforGeeks")
print("The totalNum of Vowels :", numVowels)


#Sol2

def findTotalVowels(str):

    vowel = {'a', 'e', 'i', 'o', 'u'}
    cVowel = 0
    for char in str:
        if char.lower() in vowel:
            cVowel+=1
    return cVowel

nVowels = findTotalVowels("Hello World")
print(nVowels)


#Sol3

def countTotalVowels(str):
    vowel = "aeiouAEIOU"
    tCount = sum(str.count(char) for char in vowel)
    return tCount

nVowels = countTotalVowels("Sachin")
print(nVowels)