class Person:
    
    def __init__(self, userName, userCollege):
        print("constructor called")

        self.name = userName
        self.college = userCollege

    def info(self):
        print(f'{self.name} is {self.college} student.')


p = Person("Aman", "RNC")
p.info()

p2 = Person("Rohan", "RNC")
p.info()