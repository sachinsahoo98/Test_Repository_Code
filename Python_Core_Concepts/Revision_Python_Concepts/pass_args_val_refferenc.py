
def modifyMutableList(inputList):
    inputList.append(4)
    print("The Modified List is :", inputList)

def modifyImmutableInteger(inputNum):
    inputNum+=20
    print("The Modified Number is:", inputNum)


initList = [1, 2, 3]
print("The initial list is:", initList)
modifyMutableList(initList) # demonstrating pass by reference to function
print("The final list after modified is:", initList)

inputNo = 50
print("The initial number is:", inputNo)
modifyImmutableInteger(inputNo) # demonstrating pass by value to function
print("The final number after modified is:", inputNo)