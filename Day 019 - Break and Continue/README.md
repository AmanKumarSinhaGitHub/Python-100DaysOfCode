# Break and Continue Statements in Python

This README provides an explanation of the `break` and `continue` statements in Python and demonstrates their usage with examples.

## Break Statement

The `break` statement is used to exit or terminate a loop prematurely. When a `break` statement is encountered within a loop (such as `for` or `while`), the loop is immediately terminated, and the program execution continues with the next statement after the loop.

### Syntax

```python
for item in sequence:
    if condition:
        break
    # Code to be executed
```

### Example

```python
# Example using break statement
for i in range(1, 10):
    if i == 6:
        break
    print(i)
```

Output:
```
1
2
3
4
5
```

In this example, the `for` loop iterates over the range from 1 to 10. When `i` equals 6, the `break` statement is executed, causing the loop to terminate. Therefore, the numbers 1 to 5 are printed, and the loop is exited.

## Continue Statement

The `continue` statement is used to skip the current iteration and proceed to the next iteration of a loop. When a `continue` statement is encountered within a loop, the remaining code inside the loop for that iteration is skipped, and the loop proceeds to the next iteration.

### Syntax

```python
for item in sequence:
    if condition:
        continue
    # Code to be executed
```

### Example

```python
# Example using continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:
```
1
2
4
5
```

In this example, the `for` loop iterates over the range from 1 to 6. When `i` equals 3, the `continue` statement is executed, and the rest of the code inside the loop for that iteration is skipped. The loop then proceeds to the next iteration. Therefore, the numbers 1, 2, 4, and 5 are printed, **while 3 is skipped.**

## Conclusion

The `break` and `continue` statements are powerful control flow statements in Python that allow you to alter the execution of loops. Understanding their usage can help you write more efficient and flexible code.

Use the `break` statement when you want to exit a loop prematurely, such as when a specific condition is met. Use the `continue` statement when you want to skip the rest of the code for the current iteration and move on to the next iteration.

