"""
Python | Maximum frequency character in String
"""

def findMaximumFrequency(inputStr):

    frequency_dict = {}
    for char in inputStr:
        if char not in frequency_dict:
            frequency_dict[char]=1
        else:
            frequency_dict[char]+=1

    return max(frequency_dict, key=frequency_dict.get)

print(findMaximumFrequency("GeeksforGeeks"))