class Animal:
    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Dog(Mammal):
    def bark(self):
        print("Barking...")

# Create an object of Dog class
dog = Dog()
dog.eat()   # Inherited from Animal
dog.walk()  # Inherited from Mammal
dog.bark()  # Defined in Dog
