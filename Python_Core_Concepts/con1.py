"""
What's __init__ function in python?

__init__ is a special constructor method in python which is used to allocate memory & is called/invoked as soon as the
object/instance of the class is created.
Every class consists of __init__ method which is called dynamically by python interpreter even if its not defined by
the programmer inside class.

It helps in distinguishing the methods and attributes of class from local variables.

"""

#code1

class Student:

    def __init__(self, name, rollNo, address):
        print("Init Method Called, Instanting on Student Obj", self)
        self.name = name
        self.rollNo = rollNo
        self.address = address
        print("Init Method Completed")

    def showDetails(self):
        print("Student Details are:", self.name, self.rollNo, self.address)

s1 = Student("Sachin", 26, "Barang")
s1.showDetails()

#code2

class Student:

    def getDetails(self, name, rollNo, address):
        self.name = name
        self.rollNo = rollNo
        self.address = address

    def showDetails(self):
        print("Student Details are:", self.name, self.rollNo, self.address)

s2 = Student()
s2.getDetails("Sourav", 34, "Dadhapatna")
s2.showDetails()
