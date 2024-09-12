class Employee:
    def __init__(self, name, salary):
        self.__name = name  # private member
        self.__salary = salary  # private member

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

emp = Employee("Charlie", 55000)
print(emp.get_name())
emp.set_name("Charlie Brown")
print(emp.get_name())
