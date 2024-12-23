class Animal:
    species = "mamaal"
    def __init__(self, name, age):
        self.age = age
        self.name = name

    @staticmethod
    def calc_age_as_per_humans(age):
        return age * 7

animal1 = Animal("Lily", 2)
animal1.species = "Birds"
print(animal1.species)
print(animal1.calc_age_as_per_humans(2))
animal2 = Animal("Oph", 7)
print(animal2.species)