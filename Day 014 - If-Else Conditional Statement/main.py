# if-else

age = int(input("Enter Your Age: "))

if(age>18):
    print("You can Drive")
else:
    print("Don't Drive")


# elif
money = 120

if(money<100):
    print("You have less than 100 Rupees")
elif(money<150):
    print("You have less than 150 Rupees")
else:
    print("You have more than 150 Rupees")

# Nested if else statements

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

# Comparison operators

print(10<20) # True
print(10<=20) # True

print(10>20) # False
print(10>=20)  # False

print(10==20) # False
print(10!=20) # True

# Logical Operators

print(10<20 and 30<50) # True
print(10<20 or 30>15) # True
print(not (4==4)) # False