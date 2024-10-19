"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""
from math import factorial

#Sol1
"""
1. Recursive Approach
2. Take number through a function, and multiply it until it reaches factorial of 0 which is 1. again call the function with n-1 number.
3. return current number * fn(n-1)
"""

def calculateFactorial(number)-> int:

    #base condition
    if number == 0:
        return 1
    else:
        return number * calculateFactorial(number-1)

result = calculateFactorial(int(input("Enter whose factorial is to be calculated \n")))
print(result)

#Sol2
"""
1. Looping Approach
2. Take a while loop since we have the knowledge about the end value for which factorial is to be calculated
3. multiply the number with n-1 until is reaches 0 or 1
"""
def calcFactorial(num) -> int:

    #Loop through numbers
    factorial = 1
    while(num > 0):
        factorial = factorial * num
        num+=1
    return factorial

resultFinal = calculateFactorial(int(input("Enter whose factorial is to be calculated \n")))
print(resultFinal)