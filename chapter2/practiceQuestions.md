# Chapter 2 Practice Questions

1. What are the two values of the Boolean data type? How do you write them?<br> 
    **True and False with capital T and F**

2. What are the three Boolean operators?<br>
    **and, or, and not**

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to)<br> 
    **True and True: True | True and False: False | False and True: False | False and False: False**<br>
    **True or True: True | True or False: True | False or True: True | False or False: False**<br>
    **not True: False | not False: True**

4. What do the following expressions evaluate to?
    **(5 > 4) and (3 == 5): False**<br>
    **not (5 > 4): False**<br>
    **(5 > 4) or (3 == 5): True**<br>
    **not ((5 > 4) or (3 == 5)): False**<br>
    **(True and True) and (True == False): False**<br>
    **(not False) or (not True): True**<br>

5. What are the six comparison operators?<br>
    **==, !=, >, <, =>, <=**

6. What is the difference between the equal to operator and the assignment operator?<br>
    **Assignment copies first value over to the second. Equal to is the same general function as mathematics; One is exactly the same as the other, evaluates to a Boolean.**

7. Explain what a condition is and where you would use one.<br>
    **You use a condition when you want to only execute a certain bit of code if a requirement is met. If this, do that. Otherwise, do this. Etc.**

8. Identify the three blocks in this code:<br>
    ```python
    spam = 0
    if spam == 10:
        print('eggs') ➊
        if spam > 5:
            print('bacon') ➋
        else:
            print('ham') ➌
        print('spam')
    print('spam')
    ```

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.<br>
    **Answered in [pQuestion9.py](pQuestion9.py)**

10. What keys can you press if your program is stuck in an infinite loop?<br>
    ``ctrl + c``

11. What is the difference between break and continue?<br>
    **Break exits the current loop and resumes execution of the rest of the program. Continue goes back to the beginning of the current loop.**

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?<br>
    **range(10) counts from 0 up to, but not including, 10**<br>
    **range(0, 10) counts from the first number (0) up to, but not including, the second number (10)**<br>
    **range(0, 10, 1) counts from the first number (0) up to, but not including, the second number (10), in increments/steps of the third number (1)**<br>
    **Essentially, they each do the same thing.**

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop<br>
    **(In [pQuestion13a.py](pQuestion13a.py) and [pQuestion13b.py](pQuestion13b.py))**

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?<br>
    ```python
    spam.bacon()
    ```

- Extra Credit: Look up the `round()` and `abs()` functions on the internet, and find out what they do. Experiment with them in the interactive shell.<br>
    **`round()` rounds depending on given arguments**<br>
    **`abs()` finds the absolute value**