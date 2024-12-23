"""
Taken a input list
sort the list based on the length of the letters
"""



def sortList(inputList):
    testFn = lambda x : len(x)
    return sorted(inputList, key=testFn, reverse=False)

print(sortList(["Jithin", "Arunima", "Akhil", "Matthew", "Benjamin"]))