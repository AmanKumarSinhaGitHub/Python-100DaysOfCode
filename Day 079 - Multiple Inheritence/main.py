class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

d1  = DancerEmployee("Kathak", "Shivani")
print(d1.name)
print(d1.dance) 
d1.show() 


print(DancerEmployee.mro())