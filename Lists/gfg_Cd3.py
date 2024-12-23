"""
Interchange first and list elements of list

1. by using assignment operator : a[0], a[n-1] = a[n-1], a[0]
2. by using tuple
3. by using a temporary variable
4. by slicing the string if length greater than 2 and returning modified splitted string
"""


def swapElements(testList):
    length = len(testList)
    testList[0], testList[length-1] = testList[length-1], testList[0]
    return testList

def swapElementTemp(testList):
    first = testList[0]
    testList[0] = testList[-1]
    testList[-1] = first
    return testList

def swapElementTuple(testList):
    testTuple = testList[0], testList[-1]
    testList[-1], testList[0] = testTuple

def swapsplitList(testList):
    lst = testList[-1:] + testList[1:-1] + testList[:1]
    return lst

testListParam = [2,3,7,9]
print("Initial List is:", testListParam)
print("Final List is:", swapElements(testListParam))

print("After 2nd time Change:", testListParam)
print("Final List is:", swapElementTemp(testListParam))

print("After 3rd time Change:", testListParam)
print("Final List is:", swapElementTuple(testListParam))

print("After 4th time Change:", testListParam)
print("Final List is:", swapsplitList(testListParam))