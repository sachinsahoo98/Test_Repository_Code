"""
To check if a string has all unique characters

Input : abacde
Output: False, a repeated twice

Input: abcde
Output: true, no value is repeated
"""

"""
1. approach1
-----------
Iterate through each character of the string.
and store the count of each character in a mapping
if there is any key which has mapping value greater than 1 then the string is not unique
"""

def checkUniqueString(testString):

    dictMapping = {}
    for char in testString:
        if char not in dictMapping:
            dictMapping[char] = 1
        else:
            dictMapping[char]+=1

    return any([value for value in dictMapping.values() if value > 1])

result = checkUniqueString("sachin")
if result:
    print("String is not unique")
else:
    print("Unique String")

"""
Approach2:
1. create an variable of empty set type that will store each char from the inputstr.
2. now iterate through each element in the string if the same element is present in the set it returns false.
3. if not add the element to the string.
"""

def checkDups(inputString):
    outputString = set()
    for char in inputString:
        if char in outputString:
            return False
        outputString.add(char)
    return True

print(checkDups("sahoo"))


