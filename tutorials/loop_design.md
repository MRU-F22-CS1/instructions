# Loop Design

## Introduction
This tutorial is intended to get you used to designing loops and recognizing common patterns. In small groups, working on the whiteboard or paper, work through the following exercises. You can check your answers using the Python interpreter, but try to solve them by hand first.

## Loop Design Steps
When designing loops, consider the following steps:
1. decide what to iterate (this will be placed in the loop body)
2. decide on a loop control variable (LCV)
3. decide on the terminal condition(s)
4. decide on the initial condition(s)
5. decide how to update the LCV

## Tracing loops
The following code fragment is supposed to add up all the multiples of five between 5 and 50 (inclusive), but it has a **logic** error.

```python
sum = 0
count = 5
while count <= 50:
   sum = sum + count
   count = count + 1

print("The sum is", sum)
```

1. Identify the:
   1. Body of the loop (statements to iterate)
   2. Loop Control Variable (LCV)
   3. Terminating conditions
   4. Initial conditions
   5. LCV update
2. Trace the code to see what it does. You need only trace enough to know what is happening, not every single iteration.
3. Describe what the code is actually doing.
4. Fix the code so that it actually sums the multiples of five between 5 and 50 (inclusive).

## Designing Loops
1. Write and test a Python function that implements the following logic:
    ```plaintext
    read a character from the user
    vowel_count = 0
    while the character is not an exclamation mark
        if the character is a vowel
            increment vowel_count
        read in a new character
    
    return vowel_count
    ```
    > Can you identify the LCV, conditions, and update? What is this function doing?
2. Using the [loop design steps](#loop-design-steps) listed above, design and write an algorithm for a loop which reads **10 integers** and prints out the largest.

3. Re-design your solution to the previous problem so that the loop reads *all* of the integers entered by a user until an **empty string** is input. Once more, print the largest.
    > Hint: you will need to test if the string is empty **before** casting user input to an integer.

## Extra Tracing Challenge
1. Consider the following Python code:
    ```python
    choice = int(input("Enter a positive integer >= 2: "))
    num_divisors = 0
    possible_divisor = 2

    while possible_divisor <= choice // 2:
        if choice % possible_divisor == 0:
            print("D", end="")
            num_divisors += 1
        else:
            print(".", end="")
        
        possible_divisor += 1

    if num_divisors == 0:
        print(" prime!")
    else:
        print(f" not prime ({num_divisors} divisors)")
    ```

    Answer the following:
   1. identify the loop body
   2. identify the loop control variable
   3. identify its pre-loop initialization point
   4. identify the loop test
   5. what is the termination condition?
   6. specifically, what would the termination condition be for an input of 7?
   7. identify the update of the loop control variable
   8. what is the common loop pattern?
   9. what problem is this loop solving?

2.  Trace the above for inputs of 11 and then 12.
