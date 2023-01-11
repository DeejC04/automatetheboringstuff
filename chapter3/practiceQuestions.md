# Chapter 3 Practice Questions

1. Why are functions advantageous to have in your programs?<br>
    **Functions allow you to separate code into sections that can be isolated. They can also avoid being repetitive/copy-pasting, as well as help with abstraction.**

2. When does the code in a function execute: when the function is defined or when the function is called?<br>
    **when the function is called**

3. What statement creates a function?<br>
    ```python
    def function_name()
    ```

4. What is the difference between a function and a function call?<br>
    **A function is the definition of the function and what it does. A call executes that function.**
    
5. How many global scopes are there in a Python program? How many local scopes?<br>
    **There is only a single global scope. At any given time, there will be at max one local scope (that of the function being executed/called)**

6. What happens to variables in a local scope when the function call returns?<br>
    **The variables are destroyed.**

7. What is a return value? Can a return value be part of an expression?<br>
    **A return value is the value that a function evaluates to. It can be used as part of an expression**

8. If a function does not have a return statement, what is the return value of a call to that function?<br>
    ```python
    None
    ``` 
    **(Not that there's no return statement. There is one, literally called "None")**

9. How can you force a variable in a function to refer to the global variable?<br>
    **Add the global command right before the variable.**
    ```python
    global variable_name
    ```

10. What is the data type of None?<br>
    `NoneType`

11. What does the import areallyourpetsnamederic statement do?<br>
    Imports a module called `areallyourpetsnamederic`

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?<br>
    ```python
    spam.bacon()
    ```

13. How can you prevent a program from crashing when it gets an error?<br>
    **`try` and `except`**

14. What goes in the try clause? What goes in the except clause?<br>
    **`try`: the program that may crash**<br>
    **`except`: is followed by the possible error it may produce, then under it (indented) is what the progarm should do instead**
    ```python
    try:
        # code
    except WhateverError:
        # Type what to do in case of exception here
    ```

## **Practice Projects**

For practice, write programs to do the following tasks.

### ***The Collatz Sequence***<br>
Write a function named `collatz()` that has one parameter named `number`. If number is even, then `collatz()` should print `number // 2` and return this value. If `number` is odd, then `collatz()` should print and return `3 * number + 1`.

Then write a program that lets the user type in an integer and that keeps calling `collatz()` on that number until the function returns the value `1`. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the *Collatz sequence*, sometimes called “the simplest impossible math problem.”)

Remember to convert the return value from `input()` to an integer with the `int()` function; otherwise, it will be a string value.

Hint: An integer `number` is even if `number % 2 == 0`, and it’s odd if `number % 2 == 1`.

The output of this program could look something like this:

```
Enter number:
3
10
5
16
8
4
2
1
```

### ***Input Validation***

Add `try` and `except` statements to the previous project to detect whether the user types in a noninteger string. Normally, the `int()` function will raise a `ValueError` error if it is passed a noninteger string, as in `int('puppy')`. In the `except` clause, print a message to the user saying they must enter an integer.

Solution to ***The Collatz Sequence*** with ***Input Validation***