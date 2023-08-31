# Decorators in Python are functions that modify the behavior of other functions.

# They are often used to add functionality to existing functions without changing their source code.

# Decorators are applied using the "@" symbol above a function definition. 

# They receive the original function as an argument, and usually return a new function that enhances or alters the behavior of the original function.


def greet(fx):
    
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    
    return mfx


@greet
def hello():
    print("Hello World, I am Aman")

hello()




