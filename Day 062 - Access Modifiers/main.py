class MyClass:

    def __init__(self):
        self.publicVar = "I'm public"
        self._protectedVar = "I'm protected"
        self.__privateVar = "I'm private"

# Create an instance of the class
obj = MyClass()

# Access public attribute
print(obj.publicVar)

# Access protected attribute (convention)
print(obj._protectedVar)

# Access private attribute (name mangling)
print(obj._MyClass__privateVar)