"""
Input : test_list = [“geeksforgeeks is best for geeks”], chr_list = [‘e’, ‘b’, ‘g’, ‘f’]
Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2}
Explanation : Frequency of certain characters extracted.

"""

def generateFrequency(testList, charList):
    outputString = "".join(testList).replace(" ", "")
    dictFrequency = {}
    for char in charList:
        countOccurance = outputString.count(char)
        if countOccurance > 0:
            dictFrequency[char] = countOccurance
    return dictFrequency

print(generateFrequency(["geeksforgeeks is best for geeks"], ['e', 'b', 'g', 'f']))

