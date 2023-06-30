# Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 
# The for Loop
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

## Example: iterating over a string:

```python 
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```
## Output:

A, b, h, i, s, h, e, k,
 

## Example: iterating over a list:

``` python 
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```
## Output:

Red\
Green\
Blue\
Yellow

Similarly, we can use loops for lists, sets and dictionaries.

--- 
## range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

## Example:
```python
for k in range(5):
    print(k)
```
## Output:

0\
1\
2\
3\
4\
Here, we can see that the loop starts from 0 by default and increments at each iteration.

 

But we can also loop over a specific range.

## Example:
```python
for k in range(4,9):
    print(k)
```
## Output:

4\
5\
6\
7\
8

## Example: 
### Generating a sequence of numbers from 1 to 10 with a step of 2

```python
for num in range(1, 11, 2):
    print(num)
```

## Output
1\
3\
5\
7\
9

In this example, the range() function is called with three arguments: _start is 1, stop is 11 (exclusive), and step is 2._ The loop iterates from 1 to 10 (inclusive), incrementing by 2 in each iteration.

---
## Note :
The range() function in Python is used to generate a sequence of numbers. It can take up to three arguments: `start`, `stop`, and `step`. 

* The start argument is optional, and if not provided, it defaults to 0. 

* The stop argument is required and specifies the end value (exclusive) of the sequence. 

* The step argument is also optional and determines the increment between numbers in the sequence. 