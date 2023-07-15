# Python Docstrings

Python docstrings are string literals that appear immediately after the definition of a function, method, class, or module. They are used to document the purpose, parameters, return values, and examples of usage for the associated code.

## Example

```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)
```

In this example, the docstring `'''Takes in a number n, returns the square of n'''` provides a brief explanation of what the `square()` function does.

Output:
```
25
```

Here is another example demonstrating a more detailed docstring:

```python
def add(num1, num2):
    """
    Add up two integer numbers.
    This function simply wraps the ``+`` operator and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
```

In this example, the docstring provides detailed information about the purpose, parameters, return value, related functions, and examples of usage for the `add()` function.

## Python Comments vs Docstrings

Python Comments are used to provide explanatory notes or descriptions within the code. They are completely ignored by the Python interpreter and serve as aids for programmers.

Python docstrings, on the other hand, are specifically used to document functions, methods, classes, or modules. They are accessible using the `__doc__` attribute of the respective object.

### Accessing Docstrings

To access the docstring of a function, method, class, or module, you can use the `__doc__` attribute.

Example:

```python
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```

Output:
```
Takes in a number n, returns the square of n
```

By utilizing docstrings, you can effectively document your code, making it more readable, maintainable, and understandable for both yourself and other developers.

---



# PEP 8
PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

# The Zen of Python
Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, only 19 of which have been written down.
```Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those! 
```

## Easter egg

To see the Easter egg related to The Zen of Python, you can run the following Python code in your `Terminal`:


### Windows User
```python
# If you are in windows

python

import this
```

### Mac User
```python
# If you are in windows

python3

import this
```


