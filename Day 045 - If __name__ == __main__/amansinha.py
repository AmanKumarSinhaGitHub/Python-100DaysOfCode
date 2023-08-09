def welcome():
    print("Welcome! Welcome! Welcome!")

print("This is amansinha.py")
print(__name__)

# This means if this file run through amansinha.py; 
# then call welcome
# That means if some file import amansinha, then this "wecome" will not called automatically.
if __name__ == "__main__":
    welcome()