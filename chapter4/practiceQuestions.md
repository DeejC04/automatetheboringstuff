# Chapter 4 Practice Questions

1. What is `[]`?<br>
    **Empty list value**

2. How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)
    ```python
    spam[2] = 'hello'
    ```

For the following three questions, let’s say `spam` contains the list `['a', 'b', 'c', 'd']`.

3. What does `spam[int(int('3' * 2) // 11)]` evaluate to?<br>
    `'d'`

4. What does `spam[-1]` evaluate to?<br>
    `'d'`

5. What does `spam[:2]` evaluate to?<br>
    `['a', 'b']`

For the following three questions, let’s say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.

6. What does `bacon.index('cat')` evaluate to?<br>
   `1`

7. What does `bacon.append(99)` make the list value in bacon look like?<br>
    `[3.14, 'cat', 11, 'cat', True, 99]`

8. What does `bacon.remove('cat')` make the list value in bacon look like?<br>
    `[3.14, 11, 'cat', True]`

9. What are the operators for list concatenation and list replication?<br>
    **`+` is for concatenation and `*` is for replication.**

10. What is the difference between the append() and insert() list methods?<br>
    **`append()` will add whatever is within the parentheses to the end of the string.** <br>
    **`insert()` requires two arguments. The first is what list value it should replace. The second is what the new replacement value is.**

11. What are two ways to remove values from a list?
    ```python
    listname.remove()
    ```

    **Include the arguments (what to be removed) within the parentheses.**
    ```python
    del listname[]
    ```
    
    **Put the index of the value to be removed inside of the brackets.**

12. Name a few ways that list values are similar to string values.

13. What is the difference between lists and tuples?

14. How do you type the tuple value that has just the integer value `42` in it?

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

17. What is the difference between `copy.copy()` and `copy.deepcopy()`?<br>
    **`copy.copy()` copies the list.**<br>
    **`copy.deepcopy()` copies lists within the list being copied.**
    