# Define the base class Employee
class Employee:
    # Constructor to initialize name and ID
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    # Method to show employee details
    def showDetails(self):
        print(f'Name: {self.name}, ID: {self.id}')

# Create an instance of Employee
emp1 = Employee("Aman", 213184)
emp1.showDetails()  # Output: Name: Aman, ID: 213184

# Inheritance: Programmer class inherits from Employee
class Programmer(Employee):
    
    # Constructor to initialize name, ID, and programming_language
    def __init__(self, name, id, programming_language):
        super().__init__(name, id)  # Call the base class constructor
        self.programming_language = programming_language
    
    # Method to set the programming language
    def setProgrammingLanguage(self, programming_language):
        self.programming_language = programming_language
    
    # Method to show the programming language
    def showLanguage(self):
        print(f'Programming Language: {self.programming_language}')

# Create an instance of Programmer
pro1 = Programmer("Anand", 213102, "Python")
pro1.showLanguage()  # Output: Programming Language: Python

# Change the programming language and show it
pro1.setProgrammingLanguage("Java")
pro1.showLanguage()  # Output: Programming Language: Java
