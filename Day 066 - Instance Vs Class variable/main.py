class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)


obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2
print(MyClass.class_variable) # Output: 2









class MyClass2:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass2("Aman")
obj2 = MyClass2("Anand")

obj1.print_name() # Output: Aman
obj2.print_name() # Output: Anand