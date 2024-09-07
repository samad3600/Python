from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()

dog.sound()  # Output: Bark
dog.sleep()  # Output: This animal is sleeping

cat.sound()  # Output: Meow
cat.sleep()  # Output: This animal is sleeping
