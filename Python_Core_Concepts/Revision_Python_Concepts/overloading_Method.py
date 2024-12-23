
class MathOperations:

    def add(self, *args):
        return sum(args)

    def multiply (self, num1, num2):
        return num1 * num2

    def multiply(self, num1, num2, num3= 1):
        return num1 * num2 * num3


MathObj = MathOperations()
summation = MathObj.add(4, 5, 9)
print("Summation Value is:", summation)
mult1 = MathObj.multiply(3, 2)
mult2 = MathObj.multiply(3, 4, 5)
print("Multiplication 1:",mult1,"\nMultiplication 2:", mult2)