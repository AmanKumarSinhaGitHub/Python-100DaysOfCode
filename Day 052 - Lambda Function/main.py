# function to double the num
def double(x):
    return x * 2

print(double(5))

# lambda fuction to double the num
double = lambda x: x * 2
print(double(5))





def average(x, y, z):
    return (x + y + z) / 3

print(average(5, 10, 15))


average = lambda x, y, z: (x + y + z) / 3
print(average(5, 10, 15))




def add6(avg, num):
    return 6 + avg(num)/2

print(add6(lambda x: x+x, 10))