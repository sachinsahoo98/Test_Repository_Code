"""
Python | Maximum frequency character in String

"""

def findMaxFrequency(inpstr):

    dict = {}
    for char in inpstr:
        if char not in dict:
            dict[char] = 1
        dict[char]+=1
    return max(dict, key=dict.get)

print(findMaxFrequency("GeeksforGeeks"))