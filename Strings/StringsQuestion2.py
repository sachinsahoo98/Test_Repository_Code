"""
Implement a method to perform basic string compression using the counts of repeated characters. For ex: "aaaabbccc" -> "a4b2c3"

Approach:
1: create an empty output string.
2. traverse each char of the string and store the count of each char by updating counter variable until the char is same.
if char gets changed, count again falls backs to zero. and output string will contain char along with count of the char
3. this will go upto the last characters
4. return the final string
"""



def checkStringCompression(inputString):
    resultantString =""
    dictResultant = {}
    for char in inputString:
        if char not in dictResultant:
            dictResultant[char] = 1
        else:
            dictResultant[char]+= 1

    for key, value in dictResultant.items():
        resultantString += key + str(value)
    return resultantString

print(checkStringCompression("aaaabbcccdeefff"))



def checkTestStringOutput(testString):
    result = ""
    count = 1
    for value in range(1, len(testString)):
        if testString[value] == testString[value -1]:
            count+=1
        else:
            count = 1
            result+= testString[value-1] + str(count)

    result += testString[-1] + str(count)
    return result
print(checkTestStringOutput("television"))