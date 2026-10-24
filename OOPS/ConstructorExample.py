class Constructorexample:

    def __init__(self, name):
        self.name = name# This is an instance variable. It is used to store the name of the employee.
        print("Constructorexample Created")#This print statement is executed when the object emp1 of the class is created. The __init__ method is called automatically when the object is created. It is used to initialize the attributes of the class. The __init__ method is a special method in python. It is called a constructor. It is used to create an object of the class. The __init__ method can take parameters. The parameters are passed to the __init__ method when the object is created. The parameters are used to initialize the attributes of the class.
emp1 = Constructorexample('Himanshu')# Creating an object of the class Constructorexample. emp1 is the name of the object. The object is an instance of the class. It is created using the class name followed by parentheses. The object can access the attributes and methods defined in the class. Instantiation is the process of creating an object from a class.
print(emp1.name)# This print name of the employee.

#control+/ is use for miltiple line comment in python.

class Employee:
    company = "Infosys"# This is a class variable. It is used to store the name of the company. 
    # It is shared by all instances of the class. It is defined inside the class but outside any method. 
    # It can be accessed using the class name or using the object name. It can be modified using the class 
    # name or using the object name. It can be deleted using the class name or using the object name.
    def __init__(self, name):
        self.name = name

    # A static method is a method that belongs to the class rather than an instance of the class. 
    # It can be called on the class itself, without creating an instance of the class. 
    # Static methods are defined using the @staticmethod decorator. 
    # They do not have access to the instance (self) or class (cls) variables. 
    # They are used for utility functions that do not depend on the state of the object or class.
    @staticmethod
    def welcome_message():
        print("Welcome to the Company Portal!")
    
    def display(self):# This is an instance method. It uses self to access the instance variable name.
        print(self.name)

    # A class method is a method that belongs to the class rather than an instance of the class.
    # It can be called on the class itself, without creating an instance of the class.
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

# You can call it without creating an object, or via an object
Employee.welcome_message()
emp1 = Employee('Himanshu')
print(emp1.name)
print(emp1.company)# This way we can access the class variable.
emp1.display()# this is an instance method. It uses self to access the instance variable name. It can be called using the object name. It can also be called using the class name, but it will not have access to the instance variable name.
