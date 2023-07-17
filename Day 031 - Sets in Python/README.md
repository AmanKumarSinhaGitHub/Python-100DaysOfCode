# Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. 

Set items are separated by commas and enclosed within curly brackets {}. 

Sets are unchangeable, meaning you cannot change items of the set once created. 

**Sets do not contain duplicate items.**



#### Example:
```python
info = {"Rohan", 19, False, 5.9, 19}
print(info)
```
#### Output:
```
{False, 19, 5.9, 'Rohan'}
 ```

Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.



## Accessing set items: 

### Using a For loop
You can access items of set using a for loop. 

#### Example:
```python
info = {"Rohan", 19, False, 5.9}
for item in info:
    print(item)
  ```
#### Output:
```
False
Rohan
19
5.9
```


## Empty set

This creates an empty dictionary, not a set. 

```python 
s = {}  
print(type(s))  

# Output: <class 'dict'>
```

To create an empty set, use the set() constructor:

```python 
s = set()
print(type(s))  

# Output: <class 'set'>
```
---
