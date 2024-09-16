class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_name(cls, name):
        return cls(name, None)

    @classmethod
    def from_age(cls, age):
        return cls(None, age)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects using class methods
person1 = Person("Alice", 30)
person2 = Person.from_name("Bob")
person3 = Person.from_age(25)

person1.display()  # Output: Name: Alice, Age: 30
person2.display()  # Output: Name: Bob, Age: None
person3.display()  # Output: Name: None, Age: 25
