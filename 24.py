class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    def speak(self):
        print("HONK")

    alive = True

# animals = [Dog(), Cat(), Car()] This would output an error saying "'Car' object has no attribute 'speak'," this means that our car class does not meet the minimum required attribute and methods.
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
#When iterating through the list of animals, we're calling each animal speak method which our car object doesn't have, but it does have a horn method.But if we rename horn to speak, then it would work.

    print(animal.alive)
#If we were to print this without line 16 existing, we would get an error saying "'Car' object has no attribute 'alive'" but if we added it (check line 16). The car now meets the minimum necessary requirements to be considered an animal.
