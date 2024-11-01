"""
Python – Odd Frequency Characters

Input : test_str = 'geekforgeeks'
Output : ['r', 'o', 'f', 's']

Input : test_str = 'g'
Output : ['g']
"""


def findOddFrequencyChar(strInput):
    dictAlpha = {}
    for char in strInput:
        if char not in dictAlpha:
            dictAlpha[char] = 1
        else:
            dictAlpha[char] += 1

    return [value for value in dictAlpha.keys() if dictAlpha[value]%2!= 0]


print(findOddFrequencyChar("geekforgeeks"))