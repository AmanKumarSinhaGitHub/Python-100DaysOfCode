num = [20, 40, 30, 50, 10]
print(num) # [20, 40, 30, 50, 10]

print("Sort in Ascending Order")
num.sort()
print(num) # [10, 20, 30, 40, 50]

print("Sort in Descending Order")
num.sort(reverse=True) # [50, 40, 30, 20, 10]
print(num) 

list = [1,2,3,4]
print("List is : ")
print(list) # [1, 2, 3, 4]

print("Reversing the List : ")
list.reverse()
print(list) # [4, 3, 2, 1]

# Find index of an Element
num = [10,20,30,40,50, 50]
print(num.index(40)) # 3

# Count
print(num.count(50)) # 2 

# copy

a = [2,3,4]
b = a 
b[0] = 10
print(a) # [10, 3, 4]
print(b) # [10, 3, 4]
''' when we assign b = a, we are not creating a new list. 
Instead, we are creating a new reference b that points to the same list object as a. 
This means that a and b are essentially two different names for the same list in memory. 

So when we modify b[0] by setting it to 10, we are actually modifying the underlying list object that a and b both reference. 
As a result, both a and b will reflect the change because they are referring to the same list.
'''

#copy()
a = [2, 3, 4]
b = a.copy()  # or b = a[:]
b[0] = 10
print(a)  # [2, 3, 4]
print(b)  # [10, 3, 4]

'''If we want to create a separate copy of the list a so that modifying b does not affect a, 
we can use the copy() method '''

# append()
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors) # ['voilet', 'indigo', 'blue', 'green']

# insert()
list = [20,30,40,50]
list.insert(1,88)
print(list) 
# [20, 88, 30, 40, 50]

# extend()
num = [1,2,3,4]
marks = [90, 87, 54, 32, 10]

marks.extend(num)
print(marks) # [90, 87, 54, 32, 10, 1, 2, 3, 4]

# Concatenating lists
n1 = [10,20,30]
n2 = [40,50,60]
n3 = [70]
num = n1+n2+n3
print(num) # [10, 20, 30, 40, 50, 60, 70]