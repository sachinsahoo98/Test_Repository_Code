
"""
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""

def convertList(str):
    listInit = []
    stringValue = ""

    for char in str:
        if char != ",":
            stringValue+=char
        else:
            listInit.append(stringValue)
            stringValue = ""
    listInit.append(stringValue)
    return listInit

print("Converted List is:", convertList(input("Enter Comma Separated String \n")))

def convertTuple(str):
    return tuple(convertList(str))

print("Converted Tuple is:", convertTuple(input("Enter Comma Separated String \n")))
