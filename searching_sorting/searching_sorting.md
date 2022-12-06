# Searching (and sorting) lists of custom classes
<!-- Note: this is adapted from W22, where all the labs were camping themed -->

## Introduction
This is a comprehensive lab that incorporates pretty much every topic for the term - great for studying for the final! In this lab, you will be efficiently packing a bag for a camping trip by **sorting** your gear from largest to smallest.

## Part 1: Define a `Gear` class
1. Define a new class named `Gear` in a file named `gear.py`.
2. Define a **parameterized constructor** that takes two input parameters and assigns them to instance variables, one for the gear **name** and one for the **volume**. Make sure to use appropriate data types.
3. Define a `__str__` method that **returns a string** describing the gear name and volume. You may use any (appropriate) language you like.
4. Test to make sure your `Gear` class works by instantiating and printing some gear in a **conditional execution block** (`if __name__ == "__main__"`).

## Part 2: Load your gear
1. Create a **new Python file** in the same folder as `gear.py` and import your `Gear` class.
2. The file `gear.csv` contains a list of items and their volume. In your new file, write a function to read the contents of `gear.csv` and return a list of `Gear` items.
3. In your `main` function, call the previous function and print out the list of `Gear` to make sure it is loading correctly.

## Part 3: Search through your gear to find the largest item
1. In the same file as part 2, define a new function that takes a `list` of `Gear` as a parameter. Give your function a reasonable name that makes it obvious. Your function should return the largest `Gear` object in the list.
2. Design an algorithm to search through your list and find the largest item. Think about how you want to handle ties!
   > Hint: You will need a **loop** of some kind with a nested `if` statement.
3. Implement your search algorithm in your function, then test it by calling it from your `main` function. What test values should you use to ensure it's working properly?

## Stretch challenge: Sort your gear
Sorting algorithms are beyond the scope of this course, but if you'd like a challenge, you could try sorting your gear.
1. In the same file as part 2, define a new function that takes a `list` of `Gear` as a parameter and sorts it **in place**. Give your function a reasonable name that makes it obvious it's for sorting.
   > What return value should you use in your function definition?
2. Implement a **sorting algorithm** to sort your gear. There are many, but one of the most straightforward is the [selection sort](https://www.geeksforgeeks.org/selection-sort/). Here's some code to get you started:
    ```python
    for i in range(len(gear)):
        # Find the maximum element in the rest of the list
        # We need to add i to the max_pos because we cut off everything
        # up to i with the gear[i:] slice operation
        max_pos = your_max_func(gear[i:]) + i
                
        # Swap the maximum element with the current index position
        temp = gear[i]
        ??? # Finish the swap!
    ```
    > Hint: earlier you implemented a maximum function (`your_max_func`, whatever you named it) that returned a `Gear` object. For this algorithm, you'll need to change it to return an **index position**.
3. Test your sorting function by calling it from your `main` function, then print the list again to make sure it's sorted.
