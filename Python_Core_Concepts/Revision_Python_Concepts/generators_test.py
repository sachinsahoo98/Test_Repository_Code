
def checkGenerator():
    num = 0
    while True:
        yield num
        num+=1

for value in checkGenerator():
    if value > 100:
        break
    print(value)