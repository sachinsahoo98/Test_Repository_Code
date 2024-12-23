"""
Swap two elements
1. Using temp variable
2. Using assignment operator
"""

def swapTwoElements(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

def swapCheck(num1, num2):
    num1, num2 = num2, num1
    return num1, num2

print(swapTwoElements(4, 6))
print(swapCheck(5, 9))