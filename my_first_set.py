my_set = {1, 2, 3, 4}#one way of creating a set
#my_set = set([1, 2, 2, 3])#another value of creating a set, also duplicate values are not allowed and will not print repeated values
my_set.add(5)# 2. Add a new value
#my_set.remove(6)  # Will give error if 6 not found in the set
my_set.discard(6) # Safe remove — no error if not found
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))       # {1, 2, 3, 4, 5}
print(a.intersection(b))# {3}
print(a.difference(b))  # {1, 2}#These are very useful when comparing values — like finding new or missing records between two data sets.