# if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:
- if
- if-else
- if-else-elif
- nested if-else-elif.
## An if……else statement evaluates like this:

### if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.
### if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.
 ## Example:
```python
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```
## Output:
```
Alexa, do not add Apples to the cart.
```

# elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
### Working of an elif statement
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.\
.\
.\
.\
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

## Example:
```python
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
```
## Output:
```
Number is Zero.
```

# Nested if statements
We can use if, if-else, elif statements inside other if statements as well. \
Example:
```python
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```
Output:
```
Number is between 11-20
```
Certainly! Here's a README file section summarizing the information about comparison operators in Python:

# Comparison Operators in Python

Comparison operators in Python are used to compare the values of two operands and evaluate the resulting condition as either `True` or `False`. They are commonly used in conditions within `if` statements or combined with logical operators to form complex conditions.

## List of Comparison Operators

1. **Equal to (`==`)**: Checks if the values of two operands are equal.
   - Example: `5 == 5` evaluates to `True`.

2. **Not equal to (`!=`)**: Checks if the values of two operands are not equal.
   - Example: `5 != 3` evaluates to `True`.

3. **Greater than (`>`)**: Checks if the left operand is greater than the right operand.
   - Example: `5 > 3` evaluates to `True`.

4. **Less than (`<`)**: Checks if the left operand is less than the right operand.
   - Example: `3 < 5` evaluates to `True`.

5. **Greater than or equal to (`>=`)**: Checks if the left operand is greater than or equal to the right operand.
   - Example: `5 >= 5` evaluates to `True`.

6. **Less than or equal to (`<=`)**: Checks if the left operand is less than or equal to the right operand.
   - Example: `3 <= 5` evaluates to `True`.

## Usage and Examples

Comparison operators are commonly used in conditional statements or anywhere a comparison is required. They can be used individually or combined with logical operators to form more complex conditions.

```python
x = 5
y = 3

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```



# Logical Operators in Python

In Python, logical operators are used to combine or modify Boolean values (`True` or `False`). There are three logical operators available: `and`, `or`, and `not`. These operators allow you to create more complex conditions or modify the truth values of expressions.

## 1. `and` Operator

The `and` operator returns `True` if both of its operands are `True`. It returns `False` if any of the operands is `False`. The operator evaluates the operands from left to right and stops as soon as it encounters a `False` value, returning that value. If all operands are `True`, the last operand's value is returned.

Example:

```python
x = 5
y = 3
z = 7

if x > y and x < z:
    print("x is between y and z")  # Output: "x is between y and z"
```

In the example above, the condition `x > y and x < z` is evaluated. Both sub-conditions must be `True` for the overall condition to be `True`.

## 2. `or` Operator

The `or` operator returns `True` if at least one of its operands is `True`. It returns `False` if all operands are `False`. The operator evaluates the operands from left to right and stops as soon as it encounters a `True` value, returning that value. If all operands are `False`, the last operand's value is returned.

Example:

```python
x = 5
y = 3
z = 7

if x > y or x > z:
    print("x is greater than either y or z")  # No output
```

In the example above, the condition `x > y or x > z` is evaluated. At least one of the sub-conditions must be `True` for the overall condition to be `True`.

## 3. `not` Operator

The `not` operator is a unary operator that returns the opposite of its operand's Boolean value. If the operand is `True`, `not` returns `False`. If the operand is `False`, `not` returns `True`. It is used to negate the truth value of an expression.

Example:

```python
x = True

if not x:
    print("x is False")  # No output (since x is True, not x is False)
```

In the example above, the condition `not x` is evaluated. Since `x` is `True`, `not x` evaluates to `False`, and the code block is not executed.

Logical operators are commonly used in conditional statements (`if`, `while`, etc.) to check multiple conditions or to modify the behavior of conditions based on logical operations. They allow you to create more complex conditions and make your programs more flexible and robust.

