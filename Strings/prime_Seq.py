def isPrime(number):
    if number <=1:
        return False
    for value in range(2, int(number/2)+1):
        if number%value == 0:
            return False
    return True

def countPrime(startPoint, endPoint):
    countNum = 0
    for value in range(startPoint, endPoint):
        if isPrime(value):
            countNum+=1
    return countNum

startIndex, endIndex = map(int, input("").split())
result = countPrime(startIndex, endIndex)
print(result)