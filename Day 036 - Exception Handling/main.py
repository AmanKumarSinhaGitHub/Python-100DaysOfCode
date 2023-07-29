print("Multiplication Table\n")

num = input("Enter the number: ")

print(f"You entered : {num}")

# Let's suppose user enter a string instead of number. At that time error will occur.
# To get error or to fix it, we use {try, except}

try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num)*i}")
except Exception as e:
    print("Input Invalid, Please Try Again")
    print("Error is : ", e)






    

# You can also handle different type of error with multiple "except"

try:
    num = int(input("\nEnter a number to access array elements : "))
    arr = [10, 20, 30 ,40 ,50]
    print(arr[num])

except ValueError:
    print("Input is not a Number, Try again")

except IndexError:
    print("Array size is only 5, so Please enter num below 5")