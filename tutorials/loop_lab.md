# Loops

## Introduction
The goal of this lab is to gain more experience with loops, including counted loops, sentinel loops and nested loops.

## Debugging Loops
This section refers to the following code:

```python
def sum_all() -> int:
    """
    Sums integers entered by a user until a negative is encountered.
    """
    prompt = "Enter a positive integer to sum, or negative integer to finish: "
    number = int(input(prompt)) # the priming read
    total = 0

    while number >= 0:
        print(f"You entered {number}")
        total += number
        print(f"The running sum is {total}")
        number = int(input(prompt)) # the internal read
    
    return total

def main() -> None:
    total = sum_all()
    print(f"\nThe final sum is {total}")

main()
```

The `sum_all` function contains a loop to read input from a user and calculate the running total. The loop terminates when a negative number is entered, and the final sum is printed. This program works as described.

1. Trace the program with some sample data (input 1, 2, 3, -1). What is the expected output? Run the program to see if the result matches your trace.

2. Re-run the program and input -1 as the first input. What is the result? Is this what you would expect?

3. Error: Forgetting the priming read
    
    Edit the program by commenting out the line indicated as the priming read. What **kind** of error occurs?

4. Error: Forgetting the internal read

    Return the program to its original state and run it to make sure that it works. Now, comment out the line indicated as the internal read and run the program program. What **kind** of error occurs?

> Tip: to stop an infinite loop, click on the terminal pane in VS Code and enter the command `Ctrl + C` (or `⌘ + .` on a Mac).

## Sentinel loop: Guess again!
Create a new Python script to write a guessing game. This program should:

- Define a target number between 1 and 20 to guess using `random.randint`.
- Prompt the user to guess a number between 1 and 20 (assume the input is valid)
- If the guess does not match the target, inform the user that the guess is incorrect, then prompt the user to guess again.
- Keep track of how many guesses the user inputs and return the final count.
 
Sample program functionality, where <b><u>bold underline</u></b> indicates user input:
 
<pre class="sample">
Guess a number between 1 and 20: <b><u>5</u></b>
Sorry, 5 is not the right number 
Guess a number between 1 and 20: <b><u>4</u></b>
Sorry, 4 is not the right number 
Guess a number between 1 and 20: <b><u>3</u></b>

You guessed the number in 3 guesses!</pre>

Hints:
- You will need a `while` loop. Think about:
  - what statements need to go in the **loop body**?
  - what is your **loop control variable**?
  - what is the **stop condition**?
  - how should the condition be **initialized** and **updated**?
- You will also need to initialize a counter (accumulator) and increment it each time the loop executes
- If you're not sure where to begin, we wrote a guessing game in [Lecture 10](https://github.com/MRU-F22-CS1/sample-code-curtis/blob/651f1474822e9689038363d750101ffcca50fdd7/lecture10/slide_16.py). This time we're adding repetition.

## Counted Loops

1. Write a short Python program which reads an integer "lower bound" and an integer "upper bound" from the user, and then displays all odd integers between these bounds (inclusive).

    For this exercise, use the `while` syntax.

    A sample run of the program might look like:

    <pre>
    enter lower bound: <b><u>8</u></b>
    enter upper bound: <b><u>15</u></b>

    9
    11
    13
    15</pre>

2. Modify the previous solution so that it uses the `for` syntax instead. What are the advantages and disadvantages of `while` vs `for`?

## More Challenging

1. Write a program that prints the first 8 lines of the multiplication table up to 12 - i.e print:

    ```plaintext
    1  2  3  4  5  6  7  8  9 10 11 12
    2  4  6  8 10 12 14 16 18 20 22 24
    3  6  9 12 15 18 21 24 27 30 33 36
        . . .
    8 16 24 32 40 48 56 64 72 80 88 96 
    ```
    
    Don't worry about formatting it perfectly.
    
    >Hint: you will need to use nested loops!

2. Design and write a complete Python program that prompts the user for a positive odd number, and then displays an isosceles triangle with that base width.

    <pre>
    enter base (must be positive and odd): <b><u>5</u></b>
      *
     ***
    *****</pre>

    As always, a good way to help in problem solving is to draw pictures, and to see what should happen with sample data (e.g. we have shown you 5 – draw 7 and 9). Examine the required output to find the patterns of what must happen.

    Come up with a high-level solution in pseudocode, then design and implement the code. 

    > Hint: you can use variables as a width specifier in an f-string by wrapping the variable in `{}`. For example, the following f-strings both centre a `*` in 5 spaces:
    ```python
    print(f"{'*':^5}")
    base = 5
    print(f"{'*':^{base}}")
    ```