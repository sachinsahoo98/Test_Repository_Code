from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeSound(self):
        pass

class Dog(Animal):
    def makeSound(self):
        print("Barking!!!")

class Cat(Dog):
    def makeSound(self):
        print("Meow!!!")

DogObject = Dog()
DogObject.makeSound()
CatObject = Cat()
CatObject.makeSound()