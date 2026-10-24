data = [
    ['Name', 'Age'],
    ['Amit', 30],
    ['Neha', 28],
    ['Raj', 35],
    ['Sita', 32],
    ['Ravi', 25]
]#2 list declaration
total_age = sum(x[1] for x in data[1:])
greaterage = [x for x in data[1:] if x[1] > 30]
for x in data[1:]:# this is slicing which removed header from the list
    print(x[0])
    print(x[1])
count=len(data)-1
print(count)
average_age = total_age / count
print("Average Age:", average_age)
for person in greaterage:
    print(person[0])#for displaying name only
print("Age greater than 30: ",greaterage[0])
new_data = [data[0]] + [[x[0], x[1] + 1] for x in data[1:]]

print("Original Data:", data)
print("New Data with increased age:", new_data)

