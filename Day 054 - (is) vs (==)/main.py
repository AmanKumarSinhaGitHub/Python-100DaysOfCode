# In short, 
# ""is"" keyword compares the exact {location} of object in memory
# ""=="" keyword compares the exact {value} of object


a = 4
b = 4

# compares the exact "location" of object
print(a is b) # True
# compares the exact "value" of object
print(a == b) # True


a = 4
b = '4'

print(a == b)  # False
print(a is b)  # False

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False