#Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It refers to the bundling of data (attributes) and methods (functions) that operate on that data into a 
# single unit, typically a class. 
# Encapsulation helps to protect the internal state of an object from unintended interference and misuse 
# by restricting access to its internal representation.

#Python supports three types of access modifiers: public, protected, and private.

#1.Public Modifier Example: Public attributes and methods can be accessed from anywhere, both inside and outside the class.
class Account:
    def __init__(self, owner):
        self.owner = owner  # Public attribute

acc = Account("Alice")
print(acc.owner)  # Accessing directly: Output -> Alice
acc.owner = "Bob"  # Modifying directly: Works fine

#2. Protected Modifier Example: Protected attributes and methods are indicated by a single underscore prefix.
# By prefixing an attribute with a single underscore (_), you signal to other developers: 
# "This is intended for internal use within this class and its subclasses. Please don't modify it directly 
# from outside."
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected attribute by convention

class SavingsAccount(BankAccount):
    def display_balance(self):
        # Subclasses can safely access protected attributes
        print(f"Subclass access: ${self._balance}")

acc = SavingsAccount("Alice", 1000)
acc.display_balance()  # Output: Subclass access: $1000

# Technically possible outside, but considered bad practice:
# print(acc._balance)

#3. Private Modifier Example: Private attributes and methods are indicated by a double underscore prefix.
# By prefixing an attribute with a double underscore (__), you make it private to the class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Public method to safely interact with private data (Getter)
    def get_balance(self):
        return f"Current Balance: ${self.__balance}"

    # Public method to safely modify private data with validation (Setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount!")

acc = BankAccount("Alice", 500)

# Trying to access directly throws an error!
try:
    print(acc.__balance)
except AttributeError as e:
    print(f"Error: {e}")
    # Output: Error: 'BankAccount' object has no attribute '__balance'

# Proper way to interact using public methods:
print(acc.get_balance())  # Output: Current Balance: $500
acc.deposit(200)          # Output: Deposited $200
print(acc.get_balance())  # Output: Current Balance: $700