# Polymorphism is an OOP concept where the same interface or method can exhibit different behavior 
# depending on the object. 
class Employee:

    def calculate_bonus(self):

        return 1000


class Manager(Employee):

    def calculate_bonus(self):

        return 5000


class Director(Employee):

    def calculate_bonus(self):

        return 10000