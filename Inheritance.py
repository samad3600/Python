class Animal:
    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")

# Creating an object of the Dog class
dog1 = Dog()
dog1.eat()   # Calling base class method
dog1.sleep() # Calling base class method
dog1.bark()  # Calling derived class method
