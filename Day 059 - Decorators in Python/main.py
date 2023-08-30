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

