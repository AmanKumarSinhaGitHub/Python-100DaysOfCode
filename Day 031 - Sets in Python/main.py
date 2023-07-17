# Sets only store one occurence of any item
s = {2, 3, 4, 2, 3}
print(s)
# Output : {2, 3, 4}
print(type(s))
# Output : <class 'set'>



# The items of set stores in random order
s1 = {"Rohan", 25, 'a', 65.34}
print(s1)
# Output : {65.34, 'Rohan', 25, 'a'}



# Empty set
s2 = {}  # This creates an empty dictionary, not a set. 
print(type(s2))  
# Output: <class 'dict'>

# To create an empty set, use the set() constructor:
s3 = set()
print(type(s3))  
# Output: <class 'set'>



# Printing the value in set
info = {25, "Rohan", "Sohan", 4.5}
for value in info:
    print(value)