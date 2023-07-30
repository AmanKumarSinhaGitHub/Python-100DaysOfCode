def add():

    try:
        num1 = int(input("Enter first no : "))
        num2 = int(input("Enter second no : "))

        print (f"Sum of {num1} and {num2} is {num1+num2}")
        return 1
        
    except:
        print ("Invalid Input")
        return 0
    
    finally:
        print ("Program End")
    
    
print(add())
# In above program you can see that if user input valid input or invalid input, in both case function return
# And we know that, if a function return, it will not execute the rest code

# But you can see that finally clause code will always executed.