# from db_connection import connect_to_postgresql
from PosgreSQLdb_connection import db_cursor

#connection = None removed from here .
def add_employee(name, department, salary, city, joining_date):
    sql = """INSERT INTO employees (employee_name, department, salary, city, joining_date)
             VALUES (%s, %s, %s, %s, %s)"""
    with db_cursor() as cur:
        cur.execute(sql, (name, department, salary, city, joining_date))
        return cur.rowcount

def update_salary(name, new_salary):
    with db_cursor() as cur:
        cur.execute("UPDATE employees SET salary = %s WHERE employee_name = %s", (new_salary, name))
        if cur.rowcount > 1:    # raising here triggers the rollback in db_cursor
            raise ValueError(f"{cur.rowcount} employees are named {name!r}; update cancelled")
        return cur.rowcount     # 0 = not found, 1 = updated

def delete_employee(name):
    with db_cursor() as cur:
        cur.execute("DELETE FROM employees WHERE employee_name = %s", (name,))
        if cur.rowcount > 1:
            raise ValueError(f"{cur.rowcount} employees are named {name!r}; delete cancelled")# ValueError in Python is a built-in exception
        return cur.rowcount

def find_employees(department, name):
    sql = """SELECT employee_name, salary, city, joining_date FROM employees
             WHERE department = %s AND employee_name = %s"""
    with db_cursor(commit=False) as cur:
        cur.execute(sql, (department, name))
        return cur.fetchall()