"""
A class method as the name suggest is a method i.e tied to the class.
It takes cls as the first parameter that informs python the method to be used with the class instead of instance of class
It is used to modify class level attributes rather than the individual instance of class. and is created by adding
@classmethod decorator as prefix to the function.
It is useful in scenario when we want to operate on the class level attributes or create instances of a class in a
specific way
"""

class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    @classmethod
    def extractNameFromString(cls, inputString):
        name, ageStr = inputString.split(',')
        age = int(ageStr)
        return cls(name, age)

person1 = Person.extractNameFromString("Sachin, 35")
print(person1.name, person1.age)
