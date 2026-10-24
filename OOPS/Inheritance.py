class Employee:

    def __init__(self,name,salary):# __init__ is a special method in python. It is called a constructor. It is used to create an object of the class. The _init_ method can take parameters. The parameters are passed to the _init_ method when the object is created. The parameters are used to initialize the attributes of the class.
        #__init__() ek special method hai jo object create hone ke baad automatically run hota hai aur object ki initial values set karta hai.
        self.name = name # here self.name is an instance variable. It is used to store the name of the employee.
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)


class Manager(Employee):

    def __init__(self,name,salary,team):
        super().__init__(name,salary)#super() is used to call the constructor of the parent class Employee. 
        # It allows us to initialize the attributes of the parent class in the child class. 
        # This is important because it ensures that the child class has access to the attributes and methods of 
        # the parent class. In this case, we are calling the constructor of the Employee class to initialize 
        # the name and salary attributes of the Manager class. After that, we can initialize the team attribute 
        # specific to the Manager class.
        self.team = team

    def show_team(self):
        print(self.team)


mgr = Manager("Himanshu",2500000,8)
mgr.display()
mgr.show_team() 