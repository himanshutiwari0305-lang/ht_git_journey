class Employee:# class keyword is used to create a class in python. Employee is the name of the class. A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
    pass #pass keyword is used to create an empty class in python. It is a placeholder for future code. It is used when a statement is required syntactically but you do not want any command or code to execute.


emp1 = Employee()# Creating an object of the class Employee. emp1 is the name of the object. The object is an instance of the class. It is created using the class name followed by parentheses. The object can access the attributes and methods defined in the class. Instantiation is the process of creating an object from a class.
emp2 = Employee()
emp3 = Employee()

print(emp1)# This gives the memory address of the object emp1. The memory address is a unique identifier for the object. It is used to access the object in memory. The memory address is displayed in hexadecimal format. The memory address is different for each object created from the class.
print(emp2)
print(emp3)

print(type(emp1))# This gives the type of the object emp1. The type of the object is the class from which it was created. The type of the object is displayed as <class '__main__.Employee'>. The __main__ indicates that the class Employee is defined in the main module. The main module is the top-level script that is being executed. The class name is displayed after the __main__.