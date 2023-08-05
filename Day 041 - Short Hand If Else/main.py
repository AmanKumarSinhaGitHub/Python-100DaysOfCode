# Normal If else
a = 10
b = 20

if a > b:
    print("a")
else:
    if a == b:
        print("equal")
    else:
        print("b")


# Short hand
a = 10
b = 20

print("a") if a>b else print("equal") if a==b else print("b")







a = 10
b = 20

# it is mandatory to add else
print("a") if a<b else ""







# normal 
a = 10
b = 20

if a < b:
    c = 50
else:
    c = 0

print(c)

# Short hand
c = 50 if a<b else 0
print(c)