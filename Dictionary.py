################## Dictionary
info={
    "name":"Himanshu",
    "subject": ["python","sql"], #we can use list as value in dictionary
    "topics":("data types","loops"), #we can use tuple in dictionary
    "age":45,
    "city":"noida"
}
# We cannot use list as key in dictionary because list is mutable and unhashable, but we can use tuple as key in dictionary because tuple is immutable and hashable.
print(info)
info["name"]="Himanshu Tiwari" #we can change the value of key in dictionary, python overrite the old value here with new vlalue.
info["country"]="India" #we can add new key value pair in dictionary
print(info)

#Below is the example of Nested Dictionary.
student={
    "name":"Reyansh Tiwari",
    "subject":{"math":30,"english":20},#here for key subject to store multiple value of subject along with marks I have used nested dictionary.
    "age":10
}
print(student)# this print whole dictionary
print(student["subject"])#this print only subject dictionary
print(student["subject"]["math"])#this print only math marks from subject dictionary

