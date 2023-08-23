# map()

def cube(x):
    return x*x*x


numList = [1, 2, 3, 4, 5]
newList = []

for item in numList:
    newList.append(cube(item))

print(newList) # [1, 8, 27, 64, 125]





# We can do the same thing with the help of "map"
def cube(x):
    return x*x*x

n = [1, 2, 3, 4, 5]

a = list(map(cube, n))
print(a) # [1, 8, 27, 64, 125]






# filter()

def greaterThan4(num):
    return num>4

n = [1, 2, 3, 4, 5, 6, 7, 8]

a = list(filter(greaterThan4, n))
print(a) # [5, 6, 7, 8]





# reduce()
from functools import reduce

def mySum(a, b):
    return a+b

n = [1, 2, 3, 4]

sum = reduce(mySum, n)

print(sum)