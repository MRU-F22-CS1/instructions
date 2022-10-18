# Booleans

This tutorial is intended to get you used to working with Boolean expressions and variables. Working on paper or the whiteboard, work through the following exercises. You can check your answers using the Python interpreter, but try to solve them hand first.

1. Given the following values for **integers** `w, x, y, z`:
    
    ```python
    w = 10
    x = 5
    y = 3
    z = 8
    ```
    Evaluate the following Boolean expressions:
    1. `(x == 5 and y < 3) or (w != 0 and z < 10)`
    2. `(z > 5 or w <= 10) and x > 5`
    3. `z > 5 or (w <= 10 and x > 5)`
    4. `(y == 3 or not (w > 10)) and (not (x < 10) or (z != 5))`

2.  Given the following values for **boolean** variables `x, y, z`:

    ```python
    x = True
    y = False
    z = True
    ```

    Evaluate the following Boolean expressions:
    1. `x and y or x and z`
    2. `(x or not y) and (not x or z)`
    3. `x or y and z`
    4. `not (x or y) and z`
    5. `not (z or y) or x`
    6. `y and x and z`
    7. `not z or (y or not x)`
    8. `x or x and y`

3. Match each Boolean expression in the left (numbered) column with the equivalent expression in the right (lettered) column:

    |     |                                  |     |                     |
    | --- | -------------------------------- | --- | ------------------- |
    | 1   | `not (x != y) and y == z`        | a   | `x < y and y < z`   |
    | 2   | `not (x <= y or y < z)`          | b   | `x > y and y >= z`  |
    | 3   | `(y < z or y == z) or x == y`    | c   | `x != y or y == z`  |
    | 4   | `not (x >= y) and  not (y >= z)` | d   | `x == y or y <= z`  |
    | 5   | `not (x == y and y != z)`        | e   | `x == y and y == z` |

4. The following expressions make sense, but are incorrect according to Python's rules of syntax. Rewrite them as legal Python expressions which evaluate as intended. Assume all variables are of type `int`.

    1. x and y are greater than zero		
    2. x is equal to neither y nor z
    3. x is equal to y and z
    4. x is equal to at least one of y and z
    5. x is equal to at most one of y and z
    6. x is equal to y or z, but not both		

5. Design a function which takes a year (as an integer) and decides whether or not it is a leap year.  Do each step TWO ways - one with `if` statements, and one without!

- To begin, design and implement the function so that it determines whether or not the year is evenly divisible by 4.
- Actually, century years (divisible by 100) are an exception.  They are divisible by 4, but are not leap years. Update your function definition.
- Actually, there is one last exception: every 4th century year (divisible by 400) is a leap year after all. Update your function definition one last time.
