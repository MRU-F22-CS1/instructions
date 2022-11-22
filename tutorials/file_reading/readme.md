# Exceptions and intro to File I/O
The following exercise is intended to give you practice dealing with data files and encountering common errors.

## Trick or Treat!
The file `trick_or_treaters.txt` contains counts of numbers of trick or treaters for 100 households. Each line in the file is a single integer.

1. Write a Python function to read the trick or treaters data into a **list of integers**. Reading a file has three steps:
   1. Open the file object
   2. Read the file and do processing
   3. Close the file object
   Your function should take the file name as an **argument**, but for testing purposes you can hardcode the filename in `main`.
   > Remember that the file path is relative to your **current working directory**
2. Now that you have the list of trick-or-treat data, you can do some calculations with it. Pick **one of the following** and write a function to find:
   1. The **highest** number of trick-or-treaters OR
   2. The **average** number of trick-or-treaters OR
   3. The number of households with **over 100** trick-or-treaters OR
   4. The number of households with **exactly 21** trick-or-treaters
    > Each of these functions will look similar with an **accumulator loop**. For the purposes of this exercise, do not use Python's built-in functions or methods like `max`, `count`, or `sum`!

## Error handling
The following errors are commonly encountered with file input. You **do not** need to actually handle them with `try/except` (though you can as an extra challenge), but think about how you might approach dealing with these issues.

1. Call your file reading function with an incorrect file name, like `truck_or_treaters`. What happens? How might you handle this so that instead of a runtime error your function returns an **empty list**?
2. Open `trick_or_treaters.txt` in a text editor and add an **empty line** somewhere in the middle. Fix your function call so that it loading the appropriate file. What happens? How would you handle this error?
3. Now, modify one of the lines of `trick_or_treaters.txt` so that it has a `float` instead of an `int` (e.g. change `30` to `30.0`). What kind of error occurs this time? How would you deal with it?
4. Finally, modify `trick_or_treaters.txt` so that it has **two numbers** on one line. What kind of error happens this time? How would you handle this unexpected input?