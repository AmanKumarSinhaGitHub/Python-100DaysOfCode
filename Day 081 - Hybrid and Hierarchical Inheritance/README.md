# Hybrid Inheritance in Python
Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

In Python, hybrid inheritance can be implemented by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

## Syntax
The syntax for implementing Hybrid Inheritance in Python is the same as for implementing Single Inheritance, Multiple Inheritance, or Hierarchical Inheritance.


Here's the syntax for defining a hybrid inheritance class hierarchy:
```python 
class BaseClass1:
  # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods

```
## Example
Consider the example of a `Student` class that inherits from the `Person` class, which in turn inherits from the `Human` class. The `Student` class also has a `Program` class that it is associated with.

```python
class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def show_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
    
  def show_details(self):
    Human.show_details(self)
    print("Address:", self.address)
    
class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
    
  def show_details(self):
    print("Program Name:", self.program_name)
    print("Duration:", self.duration)
    
class Student(Person):
  def __init__(self, name, age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
    
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()
```
In this example, the `Student` class inherits from the `Person` class, which in turn inherits from the `Human` class. The `Student` class also has an association with the `Program` class. This is an example of `Hybrid Inheritance` in action, as it uses both Single Inheritance and Association to achieve the desired inheritance structure.

To create a `Student` object, we can do the following:
```python
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()
```
### Output
```python
Name: John Doe
Age: 25
Address: 123 Main St.
Program Name: Computer Science
Duration: 4
```
As we can see from the output, the `Student` object has access to all the attributes and methods of the `Person` and `Human` classes, as well as the `Program` class through association. 

In this way, hybrid inheritance allows for a flexible and powerful way to inherit attributes and behaviors from multiple classes in a hierarchy or chain.



# Hierarchical Inheritance

Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.

Here's an example to illustrate the concept of hierarchical inheritance in Python:
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)
```
In the above code, the `Animal` class acts as the base class for two subclasses, `Dog` and `Cat`. The `Dog` class and the `Cat` class inherit the attributes and methods of the `Animal` class. However, they can also add their own unique attributes and methods.

Here's an example of creating objects of the `Dog` and `Cat` classes and accessing their attributes and methods:

```python
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()
```
### Output:
```
Name: Max
Species: Dog
Breed: Golden Retriever
Name: Luna
Species: Cat
Color: Black
```
As we can see from the outputs, the `Dog` and `Cat` classes have inherited the attributes and methods of the `Animal` class, and have also added their own unique attributes and methods.

In conclusion, hierarchical inheritance is a way of establishing relationships between classes in a hierarchical manner. It allows multiple subclasses to inherit from a single base class, which helps in code reuse and organization of code in a more structured manner.




