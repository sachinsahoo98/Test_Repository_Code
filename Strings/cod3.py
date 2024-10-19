"""
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
"""
Approach:
1. create an empty list to store the integers.
2. Use iterator to traverse numbers between 2000 and 3200.
3. Check if current number is divisible by 7 and not divisible by 5.
4. if satisfies store append the no. to the list in form of string.
5. print the final list by joining comma between the numbers.
"""

def findNumbers():
    initList = []
    for value in range(2000, 3201):
        if value % 7 == 0 and value % 5!= 0:
            initList.append(str(value))
    return ", ".join(initList)

result = str(findNumbers())
print("Result is:", result, end="")
