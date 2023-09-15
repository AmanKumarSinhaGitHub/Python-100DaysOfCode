class Shape:

    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # OVERRIDING
    def area(self):
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius
    
areaOfCircle = Circle(5).area()
print(areaOfCircle)