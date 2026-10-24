def calculate_salary(basic,hra,da):
    total_salary = basic + (basic * hra/100) + (basic * da/100)
    return(total_salary)
def main():
    emp_name=input("Enter Employee Name ")
    basic=float(input("Enter Basic Salary "))
    hra=float(input("Enter HRA "))
    da=float(input("Enter DA "))
    x=calculate_salary(basic,hra,da)
    print(f"{emp_name}'s total salary is {x}")
main()
