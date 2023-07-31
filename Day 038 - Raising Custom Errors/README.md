## Raising Custom errors 
In python, we can raise custom errors by using the `raise`  keyword. 
```python
num = int(input("Enter a number less then 100 : "))

if (num>=100):
    raise ValueError("Please enter no less than 100")
```

In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

## Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
```python
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.
