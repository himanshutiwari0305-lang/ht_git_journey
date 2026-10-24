
###########################################################
#Example 2(b): Read from a csv File
with open("employee.csv", "r") as file:#with option will close the file automatically, 
    content = file.read()
    print(content)

#################################################################################
import csv 

with open("employee.csv", "r", encoding="utf-8-sig") as file: #this will remove special character due to file save in utf-8 format
    reader = csv.reader(file)  #for csv.reader() / csv.writer() import csv is needed at the top
    for row in reader:
        print(row)

##########################################################################
#Example 3: To create a csv file and write data into it.
#import csv

#data = [
#    ['name', 'age', 'city'],
#    ['Rekha', 30, 'Delhi'],
#    ['Himanshu', 43, 'Noida'],
#    ['Mumm', 50, 'Noida']
#]

#with open("created_filehandling.csv", "w", newline='') as file:
#    data.append(['rey', 10, 'rksh'])#to append data in csv file, not sure if it worked correctly need to check again
#    writer = csv.writer(file)
#    writer.writerows(data)
##########################################################################
#Example 4: filter the employees in noida.

#import csv

#with open("employee.csv", "r", encoding="utf-8-sig") as file:
#    reader = csv.DictReader(file)
#    employees = list(reader)  # har row ek dictionary ban jaayega
#noida_emps = [emp for emp in employees if emp["city"].lower() == "noida"]
#print(noida_emps)
#total_age = sum(int(emp["age"]) for emp in employees)
#average_age = total_age / len(employees)
#print("Average Age:", average_age)
#with open("noida_employees.csv", "w", newline='') as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])#writing the filtered data
#    writer.writeheader()
#    writer.writerows(noida_emps)


##########################################################################
#Example 5: filter the employees in noida above 40.

#import csv

#with open("employee.csv", "r", encoding="utf-8-sig") as file:
#    reader = csv.DictReader(file)
#    employees = list(reader)  # har row ek dictionary ban jaayega
#noida_emps = [emp for emp in employees if int(emp["age"])> 40]
#print(noida_emps)
#total_age = sum(int(emp["age"]) for emp in employees)
#average_age = total_age / len(employees)
#print("Average Age:", average_age)
#with open("above_40_employees.csv", "w", newline='') as file:
#    writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])#writing the filtered data
#    writer.writeheader()
#    writer.writerows(noida_emps)


##########################################################################





