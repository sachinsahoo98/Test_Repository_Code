"""
# Python 3 code to demonstrate
# Least Frequent Character in String
# naive method
"""

"""
1. Create an empty dict
2. Traverse through all character of string and store the value of each in dict in form of key, value pairs
if char is already there in dict, increament its occurance value by 1.
else add the character to dict and set the occurance value to 1.
3. find the min value from the dict values.

"""

def calculateLFC(testStr):

    frequencyChars = {}
    for char in testStr:
        if char in frequencyChars:
            frequencyChars[char]+=1
        else:
            frequencyChars[char]=1
    return min(frequencyChars, key = frequencyChars.get)

print(calculateLFC("GeeksforGeeks"))