"""
Maximum of two numbers in Python

1. Approach using the max function
2. using the if-else relational ladder

"""

class ListOperationNumbers:

    def __init__(self, test_List):
        self.test_List = test_List

    def findMax(self):
        return max(self.test_List)

    def maxUsingNative(self):
        num1, num2 = self.test_List
        if num1 > num2:
            maxElement = num1
        else:
            maxElement = num2
        return maxElement

    def findMin(self):
        return min(self.test_List)

    def minUsingNative(self):
        value1, value2 = self.test_List
        if value1 < value2:
            minElement = value1
        else:
            minElement = value2
        return minElement

testMaxObj = ListOperationNumbers([32, 41])
print("Using Max Builtin:",testMaxObj.findMax())
print("Using Native:", testMaxObj.maxUsingNative())
print("Using Min Builtin:",testMaxObj.findMin())
print("Using Native:", testMaxObj.minUsingNative())

