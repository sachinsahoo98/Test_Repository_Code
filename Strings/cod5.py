"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

#Solution

"""
Approach :
1. Create an empty dict.
2. Loop through the numbers from 1 to 10.
3. for each number calculate, number multipled by itself. 
4. store each number in dict with key = number, value = num*num
"""

def storeSquare():

    dictInitial = {}
    for value in range(1, 11):
        dictInitial[value] = value ** 2
    return dictInitial

print(storeSquare())