"""
Python – Odd Frequency Characters
Input : test_str = 'geekforgeeks'
Output : ['r', 'o', 'f', 's']

"""

def calculateFrequency(inputStr):
    frequencyDict = {}
    for char in inputStr:
        if char not in frequencyDict:
            frequencyDict[char]=1
        else:
            frequencyDict[char]+=1
    return frequencyDict

def generateOddFrequencyChar(inputDict):
    outPutList = []
    for key, frequencyValues in inputDict.items():
        if frequencyValues % 2 != 0:
            outPutList.append(key)
    return outPutList

outputDict = calculateFrequency("geekforgeeks")
outputList = generateOddFrequencyChar(outputDict)
print(outputList)