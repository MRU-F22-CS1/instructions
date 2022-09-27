# Operators and Interactive Python

## Instructions
Today's tutorial will involve some work on the computer and some on the whiteboard. Your instructor will assign you to a group of 2-3. Introduce yourselves, then begin working on the following activities.

Python uses the following arithmetic operators. This tutorial is intended to get you familiar with how these operators work, their **precedence**, and using the interactive shell.

| Name                 | Operator | Precedence | Example                        | Math equivalent                 |
| -------------------- | -------- | ---------- | ------------------------------ | ------------------------------- |
| Parentheses/brackets | `()`     | 1          | `x = (2 + 3)/2` <br> `x = 2.5` | $x = \frac{2 + 3}{5}$           |
| Exponentiation       | `**`     | 2          | `x = 3 ** 2` <br> `x = 9`      | $x = 3^2 $                      |
| Multiplication       | `*`      | 3          | `x = 3 * 2.5` <br> `x = 7.5`   | $x = 3\times 2.5 $              |
| Division             | `/`      | 3          | `x = 5 / 2` <br> `x = 2.5`     | $x = \frac{5}{2} $              |
| Integer Division     | `//`     | 3          | `x = 5 // 2` <br> `x = 2`      | N/A - round down after dividing |
| Modulo               | `%`      | 3          | `x = 5 % 2` <br> `x = 1`       | N/A - remainder after dividing  |
| Addition             | `+`      | 4          | `x = 2 + 2` <br> `x = 4`       | $x = 2 + 2 $                    |
| Subtraction          | `-`      | 4          | `x = 5 - 6` <br> `x = -1`      | $x = 5 - 6 $                    |

Python follows the same precedence as standard math (BEDMAS). When two operators of the same precedence are on the same line, the operation happens from **left to right**.

## Order of operations
On paper or a whiteboard, solve the following arithmetic expressions. 

1. `2*(20/4 + 1) + 5`
2. `4*3 / 6`
3.  `4/6 * 3`
4.  `3*4 / 6`

Next, try the following to test out the new operators `//` and `%`

1. `4//6 * 3`
2. `3*4 // 6`
3. `7 % 3`
4. `4 + 7%3 - 5`
5. `(4 + 7)%3 - 5`

On a computer (one per group), open up your terminal (Git Bash on Windows or Terminal on a Mac) and launch the Python interactive shell with either `python -i` or `python3 -i` on a Mac. Check your results. Were your calculations correct?

> Sometimes Git Bash will launch the Windows store instead of the interactive Python terminal. If this happens, you can try the following command:
    ```
    winpty python.exe
    ```

## Working with Variables
Given the following variable definitions: 

```python
x = 2.5
y = -1.5
m = 18
n = 4
```

What are the values of the following expressions? Again, evaluate first by hand, then check your work using the Python interpreter.

1. `x + n*y - (x + n)*y`
2.  `m//n + m%n`
3. `5*x - n // 5`
4. `1 - (1 - (1 - (1 - (1 - n))))`

## Translating math to code
**By hand**, write Python arithmetic expressions for each of the following. Assume the variables have already been declared and assigned. Since you are writing a math formula, it is okay for your variable names to be short (e.g. just "A").

1. $A + \frac{B}{C + D}$
2. $(X - 1)(Y -4)$
3. $\frac{-B + X}{2A}$
4. $XY^2Z$

How would you check if your expressions are correct?

## Algorithm design
You are coding an online interface to a board game called Incan Gold, where players explore a temple and try to collect as many gems as they can. Gems are split equally between each player, with any amount leftover added to a separate pile. 

Given the **total number of gems** and **number of players**, write an algorithm to calculate how many gems are received by each player and how many are leftover. The result should be displayed to the user.

Write out the steps of the algorithm in **pseudocode**, as a flowchart, or in point form, whatever makes the most sense to you.

>Hint: Before starting to design the algorithm, check your understanding by working through a couple of examples, such as 11 gems and 4 players, or 13 gems and 5 players.

## Code tracing
For each of the following code snippets, predict what will be written to the screen. You may find it helpful to write down the intermediate values of each variable when they are reassigned.

1. 
    ```python
    freeze = 32
    boil = 212
    freeze = 0
    boil = 100
    print(freeze)
    print(boil)
    ```

2. 
    ```python
    doughnuts = 6
    friends = 3
    print("We all get", doughnuts/(friends + 1), "doughnuts.")
    ```

3. 
   ```python
    doughnuts = 6
    friends = 3
    total_peeps = friends + 1
    whole_doughnuts = doughnuts // total_peeps
    leftover = doughnuts % total_peeps
    print("We all get", whole_doughnuts, "whole doughnuts!")
    print("There are", leftover, "doughnuts left over.")
    ```

4. 
    ```python
    beta = 9
    alpha = 3 * beta
    print(alpha, ",", beta)
    alpha = alpha + 1
    print("alpha,beta")
    beta = beta + beta
    print(alpha, ",", beta)
    ```
