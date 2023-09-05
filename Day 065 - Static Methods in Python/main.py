class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n
    
    # Static method don't require 'self'
    @staticmethod
    def add(a,b):
        return a+b

a = Math(5)
print(a.num)
a.addToNum(6)
print(a.num)


# static method
print(a.add(5,10))
print(Math.add(5,10))
