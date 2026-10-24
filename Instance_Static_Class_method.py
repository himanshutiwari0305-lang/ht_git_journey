class EmployeeRecord:
    # Class attribute (shared by all instances)
    target_database = "PostgreSQL_Prod"

    def __init__(self, emp_id, name, salary):
        # Instance attributes (unique to each object)
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # 1. INSTANCE METHOD
    # Uses 'self' to access and modify a specific employee's instance attributes
    def apply_performance_bonus(self, bonus_percentage):
        bonus_amount = self.salary * (bonus_percentage / 100)
        self.salary += bonus_amount
        print(f"Bonus applied to {self.name} ({self.emp_id}). New Salary: ${self.salary:,.2f}")

    # 2. CLASS METHOD
    # Uses 'cls' to act as an "Alternative Constructor" (Factory Method)
    # Parses a raw string from a file/database and creates a new object
    @classmethod
    def from_csv_row(cls, csv_line):
        # Sample csv_line: "101,Himanshu Tiwari,85000"
        emp_id_str, name, salary_str = csv_line.split(",")
        emp_id = int(emp_id_str.strip())
        salary = float(salary_str.strip())
        
        # Calls the class constructor cls(...) to return a new EmployeeRecord instance
        return cls(emp_id, name.strip(), salary)

    # 3. STATIC METHOD
    # Uses neither 'self' nor 'cls'. It is a pure helper/utility function.
    @staticmethod
    def validate_employee_id(emp_id):
        # Business Rule: Employee ID must be a positive 3-digit integer (100 to 999)
        return isinstance(emp_id, int) and 100 <= emp_id <= 999


# ==========================================
# DRIVER CODE (How to use them)
# ==========================================

# --- Using the Static Method ---
# We can validate an ID before even creating an object!
print("--- 1. Testing Static Method ---")
print(f"Is ID 105 valid? -> {EmployeeRecord.validate_employee_id(105)}")  # Output: True
print(f"Is ID 45 valid?  -> {EmployeeRecord.validate_employee_id(45)}")   # Output: False
print()

# --- Using the Class Method (Factory Constructor) ---
# Useful when reading raw data strings from ETL pipelines or CSV files
print("--- 2. Testing Class Method ---")
raw_data = "101, Himanshu Tiwari, 95000"

# Calling class method creates and returns a new object
emp1 = EmployeeRecord.from_csv_row(raw_data)
print(f"Created Object for: {emp1.name}, ID: {emp1.emp_id}, Salary: ${emp1.salary:,.2f}")
print()

# --- Using the Instance Method ---
# Operates specifically on 'emp1' instance data
print("--- 3. Testing Instance Method ---")
emp1.apply_performance_bonus(10)  # 10% bonus applied specifically to Himanshu