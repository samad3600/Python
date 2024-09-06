class Parent:
    def show(self):
        print("This is the parent class.")

class Child(Parent):
    def show(self):
        print("This is the child class.")

# Creating objects of Parent and Child classes
parent_obj = Parent()
child_obj = Child()

parent_obj.show()  # Calls Parent's show method
child_obj.show()   # Calls Child's show method
