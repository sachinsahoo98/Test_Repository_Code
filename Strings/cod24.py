"""

Input:aaabbbacfwww
Output:a3b3acfw3
"""

def updateString(inputString):
    if not inputString:
        return ""
    outputString = ""
    count = 1
    for index in range(1, len(inputString)):
        if inputString[index] == inputString[index-1]:
            count+=1
        else:
            outputString += inputString[index - 1] + str(count) if count > 1 else inputString[index - 1]
            count=1
    outputString += inputString[-1] + str(count) if count > 1 else inputString[-1]
    return outputString



inputStr = input("Enter the user string \n")
res = updateString(inputStr)
print(res)