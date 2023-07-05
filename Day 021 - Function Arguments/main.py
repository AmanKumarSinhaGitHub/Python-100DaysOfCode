def average(a,b):
    print("Average of", a, "and", b, "is", (a+b)/2)

average(10,15)
# Average of 10 and 15 is 12.5

# Dafaut argument
def average(a,b=4):
    print("Average of", a, "and", b, "is", (a+b)/2)

average(10)
# Average of 10 and 4 is 7.0

average(b=8, a=6) # We can the change order of input
# Average of 6 and 8 is 7.0


# Variable Length Argument
def average(*numbers):
    print(type(numbers)) #Tuple
    sum = 0
    for i in numbers:
        sum += i
    print("Average is ", sum/len(numbers))

average(4,5,6,7)

# Keyboard Arbitrary Arguments
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Kumar", lname = "Sinha", fname = "Aman")

# Return statement
def greeting():
    return ("Good Morining")

message = greeting()
print(message)