# Input validation loops

## Instructions
The following exercises will give you further practice writing loops and validating user input. If you're feeling really adventurous, you could try giving recursion a try.

## Exercises

### Factorial finder

The "factorial" of an integer is the product of that integer and all the positive integers less than it. It is denoted with an exclamation mark (!). So,

$$n! = n \times (n-1) \times (n-2) \times ... \times 2 \times 1$$
    
1. Write a function called `factorial` that computes the factorial of a given integer.  

    ```python
    # example use
    factorial(0)  # should return 1
    factorial(1)  # should return 1
    factorial(2)  # should return 2
    factorial(3)  # should return 6...
    ```

2. If you used a `while` loop to solve part 1, re-write your solution using a `for` loop. If you used a `for` loop, re-write your solution using a `while` loop.
 
> Extra challenge: can you find a recursive solution to this problem? Don't attempt this until you've done all the rest of the exercises!

### Password validation

Imagine you are creating an online service, and are writing the code that handles creation of user accounts. 
You must write write two Python functions to help you with your job:

1. The first function should be called `invalid_password`. It takes in a string and returns true if that string is an **invalid password**, and false otherwise. A password is considered invalid if it has fewer that 8 characters or is one of these poor password choices: 
     - "password"  (case sensitive)
     - "12345678"

    ```python
    # example use
    invalid_password("h1")           # should return True; too short!
    invalid_password("12345678")     # should return True; poor choice
    invalid_password("password")     # should return True; another poor choice
    invalid_password("PASSWORD")     # should return False; not exactly "password"
    invalid_password("w00tw00tWOO!") # should return False; everything OK!
    ```
    > Hint: The function `len` returns the length of a string
2. The second function should be called `valid_password_from_user`. It should prompt the user for a password and validate that password using a sentinel loop and the `invalid_password` function. It should return the validated password.

Once you think you have these functions working, use this code to test them:

```python
def main() -> None:
    validated_password = valid_password_from_user()
    print(f"Yay - '{validated_password}' is a valid password!")


main()
```

Here is an example run of a working final result:

> choose a password: **1234**  
> Oops - password must be at least 8 characters long and not 'password' or '12345678'!   
> choose a password: **password**  
> Oops - password must be at least 8 characters long and not 'password' or '12345678'!  
> choose a password: **12345678**  
> Oops - password must be at least 8 characters long and not 'password' or '12345678'!  
> choose a password: **password1**  
> Yay - 'password1' is a valid password!  
        
### Isosceles triangle

Design and write a complete Python program that prompts the user for a base, and then prints an isosceles triangle with that base width. If the input is **even** or **negative** then the program must terminate with an appropriate error message. 

For example:

```text
enter base (must be positive and odd): 4
Base is not a positive odd number. Exiting.
```

```text
enter base (must be positive and odd): -5
Base is not a positive odd number. Exiting.
```

```text
enter base (must be positive and odd):3

 *
***
```

```text
enter base (must be positive and odd):5

  *
 ***
*****
```

A good way to help in problem solving is to draw pictures, and to see what should happen with sample data (e.g. we have shown you 3 and 5 – draw 7 and 9). Examine the required output to find the patterns of what must happen.

Come up with a high-level solution in pseudocode, then design and implement the code. 
