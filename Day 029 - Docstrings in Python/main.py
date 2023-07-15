def showName(name):
    '''Printing the Name'''
    print("Your name is", name)

showName("Aman")
# Output : Your name is Aman

print(showName.__doc__) # Printing the docstring
# Output : Printing the Name



# docstring must be just below the function name; 
# otherwise it will not consider as a docstring and if you print that it will print "None"

def showName(name):
    print("Your name is", name)
    '''Printing the Name'''
    

showName("Aman")
# Output : Your name is Aman

print(showName.__doc__) # Printing the docstring
# Output : None



