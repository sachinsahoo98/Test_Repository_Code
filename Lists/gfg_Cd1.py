"""
Python – Ways to find length of list

1. using len function
2. using for loop and a counter variable
3. using sum method and for loop
4.
"""

class ListLengthOperation:

    def __init__(self, testList):
        self.testList = testList

    def calcLen(self):
        return len(self.testList)

    def calcLenUsingLaymans(self):
        countNumElements = 0
        for item in self.testList:
            countNumElements+=1
        return countNumElements

    def usingSumcalcLen(self):
        return sum(1 for item in self.testList)


testObject = ListLengthOperation([1, "sachin", [3, 5], 3.67, {'a': 98}, (56, 57), {87, 'sahoo'}])
print("Finding Length Using Different Methods:")
print("Builtin :", testObject.calcLen())
print("ForLoop:", testObject.calcLenUsingLaymans())
print("Sum:", testObject.usingSumcalcLen())