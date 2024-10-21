"""
Python Program to Accept the Strings Which Contains all Vowels

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present

"""

#Sol 1
def acceptString(inputStr):

    vowelList = ['a', 'e', 'i', 'o', 'u']
    vowelsCount = 0
    status = "Not Accepted"

    for vowel in vowelList:
        if vowel.upper() in inputStr or vowel in inputStr:
            vowelsCount += 1
    if vowelsCount == len(vowelList):
        return "Accepted"
    return status

res = acceptString("hellosachinsourav")
print(res)

#Sol2

def acceptString(inputStr):

    vowelList = {'a', 'e', 'i', 'o', 'u'}
    vowelsCount = set()
    status = "Not Accepted"

    for char in inputStr:
        if char.lower() in vowelList:
            vowelsCount.add(char.lower())
    if vowelsCount == vowelList:
            return "Accepted"
    return status

res = acceptString("geeksforgeeks")
print(res)