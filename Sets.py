# A set can be a mutable , but its elements must be immutable, hence you can have a set of integers, strings, 
# or tuples, but not a set of lists or dictionaries.
# A set is a collection of unique elements. 
# It is unordered and does not support indexing or slicing. 
# Sets are useful for membership testing, 
# removing duplicates from a sequence, 
# and performing mathematical operations like union, intersection, difference, and symmetric difference.

collection=set()# empty set, we cant create an empty set using {} because it will create an empty dictionary instead.
set_collection={1,2,3,4,5}# set with elements
print(collection)
print(set_collection)

collection={1,2,2,2,3,4,5,6,7,8,9,10}
print(collection)#remove duplicate elements from the set and print unique elements only.
collection.add(11)#add new element in the set
print(collection)
collection.remove(2)#remove element from the set
print(collection)
collection.add('himanshu')#adding string element in the set
print(collection)
collection.add((1,2,3))#adding tuple element in the set, since tuple is immutable we can add it in the set.
print(f'collection with tuple element: {collection}')