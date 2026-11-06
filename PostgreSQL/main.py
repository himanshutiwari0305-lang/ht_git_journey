import psycopg2
import employee_crud as crud

def ask_salary():
    while True:
        try:
            return float(input("Salary: "))
        except ValueError:
            print("Please enter a number.")

def main():
    action = input("1=add 2=update 3=delete 4=search: ").strip()
    try:
        if action == "1":
            crud.add_employee(input("Name: "), input("Department: "), ask_salary(),
                              input("City: "), input("Joining date (YYYY-MM-DD): "))
            print("Employee added.")
        elif action == "2":
            print("Updated." if crud.update_salary(input("Name: "), ask_salary()) else "Employee not found.")
        elif action == "3":
            print("Deleted." if crud.delete_employee(input("Name: ")) else "Employee not found.")
        elif action == "4":
            print(crud.find_employees(input("Department: "), input("Name: ")) or "No matching records found.")
    #except OperationalError:
    #    log.exception("Database unavailable")          # retry-worthy
    #except IntegrityError:
    #    log.exception("Row rejected by a constraint")  # data problem, don't retry
    #except DataError:
    #    log.exception("Bad value, e.g. wrong date format")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()