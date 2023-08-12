# Global Variable
x = 4
print(x) # 4

def hello():

    print("Hello")

    # local variable
    x = 5
    print(x) # 5 (printing local variable x value)

    # Local variable
    y = 10
    print(y) # 10

hello()

print(x) # 4 (printig global variable x value)

# print(y) # Error (y is local variable)


# Global variable and used inside a function
num = 10

def number():

    print(num) # 10


number()
