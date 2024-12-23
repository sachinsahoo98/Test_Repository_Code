"""
Frequency of numbers in a string
The original string is : geeks4feeks is No. 1 4 geeks
Count of numerics in string : 3
"""
import re

def calcFrequencyNum(userString):
    numericals = 0
    for char in userString:
        if char.isdigit():
            numericals+=1
    return numericals


def calcTest(userString):
    match = re.findall(r"\d+", userString)
    return len(match)

print(calcFrequencyNum("geeks4feeks is No. 1 4 geeks"))
print(calcTest("geeks4feeks is No. 1 4 geeks"))

