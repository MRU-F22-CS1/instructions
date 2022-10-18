# Assignment 3: Functions and decisions
Due on November 10, 2022, 5 PM. Note that this is a Thursday, not a Friday, due to Remembrance day.

## Video Overview

[![Click here to Watch the video](https://img.youtube.com/vi/82wMaLhdd-0/default.jpg)](https://youtu.be/82wMaLhdd-0)

## Objectives
Upon completion of this assignment, students will have had the opportunity to:
- Gain experience testing software behaviour
- Practice designing and implementing complex decision structures
- Build a program with multiple functions and function calls

## Outcome
Done **individually or in pairs**, this assignment consists of **two products**:

1. A **written description** of your testing process.
2. The **code**: a Python file that solves the following problem.

## Introduction and background information
In the distant future, where space travel has become a commonplace activity with its origins long forgotten, you are part of a team exploring an abandoned world. Much of the rubble left behind is worthless, but you stumble across a **replicator** that still appears to be functioning! This is a piece of human technology that has been lost, so you are excited to share your findings with your team.

The control labels have worn off, but there are **two buttons and a slider**. Changing these controls seems to produce different beverages. You begin playing around with the settings and decide to **duplicate** the behaviour in a text-based interface in order to understand how it works.

## Instructions
1. Visit [https://mru-replicator.fly.dev/](https://mru-replicator.fly.dev) and enter your MRU username where indicated. **Your MRU username must be correct** in order for you to receive full marks, as this defines the combinations of beverages that you receive. If you are working in partners, **choose one username** for all of your testing and implementation.
2. Keeping your username constant, modify the switches A and B and the numeric slider, pressing the "Replicate!" button for each combination. Document your experiments until you have established the behaviour.

  > Hint: think about the number of possible combinations for the switches A and B, and make sure to test exhaustively.

3. Using the provided starter code, write a Python program that duplicates the behaviour of the abandoned replicator. **Do not** prompt the user for their MRU username. When executed, your program should look something like this, where text in **bold** represents user input.
  <pre>
  Is switch A enabled? (y/n): <b>y</b>
  Is switch B enabled? (y/n): <b>n</b>
  What is the value of the numeric slider? (0-100): <b>60</b>
  Result: Tea, Earl Grey, Hot
  </pre>

## Assumptions
To make things manageable, you can assume the following:
1. The numeric slider has a logical behaviour. For example, there will not be a random single value in the middle of the range with a surprising result.
2. When writing your code, you can assume the user provides **valid input**. This means they will always enter `y` or `n` when prompted `y/n`, and will always enter an integer when prompted for the value of the numeric slider.
3. The behaviour is always the same for a given MRU username (case insensitive).

## Starter code
Follow the link to GitHub Classroom on **your section's D2L page**. This ensures that your instructor sees your submissions.

### `assign3.py`
Implement your program solution in `assign3.py`. Make sure to define your **MRU Username** where indicated in the starter code. This is used to compare your output with the website.

To provide some guidance, the starter code has several functions for you to complete. **Do not modify the function headers**. For each of the predefined functions, implement an algorithm solving the specified task. 

You may define additional functions, but **do not use techniques that have not yet been taught in class**.

### `testing_log.md`
Write your name (and the name of your partner) and record the results of your testing in `testing_log.md`. This is a Markdown format file - you can treat it like a normal text file, but if you want to get fancy with formatting, check out [this guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

If you are working in partners, **choose one username** for all of your testing and implementation.

## Grading

### F Level

It's kinda hard to get an F - I mean, you really have to want it.  

That being said, an F is possible if:

- [ ] nothing is submitted, or
- [ ] submitted code is **VERY** broken (for example, doesn't run at all), or
- [ ] submitted code runs, but doesn't even *partially* solve *any* aspect of the assignment
- [ ] some of your submitted code is plagiarized or copied from another student

### D Level 

A D Level will be given to any submission that doesn't reach the C Level, but isn't so far gone as to get an F.

### C Level
In order to receive a C level you must meet all of the following conditions:
- [ ] `get_beverage_type` returns the correct beverage for each switch combination.
- [ ] `get_temperature_desc` returns the correct strings for the **ends** of the slider.
- [ ] `get_switch_value` returns `True` or `False` when the user inputs `y` or `n`, respectively.
- [ ] Your `get_switch_value` function correctly prompts the user with the switch label and `y/n`.
- [ ] Additionally, you must provide an adequate description of your testing process.

### B Level
In order to receive a B level you must meet all of the C requirements and:
- [ ] Your `main` function must produce the expected output (e.g. as shown in step 3 of [Instructions](#instructions)).
- [ ] Your written description of your testing process must be complete and clear, without grammatical errors.

### A Level
In order to receive an A level you must meet all of the B requirements and:
- [ ] Your temperature ranges must correspond *exactly* to the temperature slider values.

> ASCII art is not required to achieve an A level, but you are welcome to add it as an additional challenge.
  
### Grade Adjustments For Code Expressiveness
Since code is meant to be read, not just run, it is very important that it expresses its intention well. If your code is hard to understand because of poorly named variables, unnecessary repetition, inconsistent style, lack of appropriate comments, or generally sloppy programming, then the submission will either wind up in the minus side of a level, or, in extreme cases, might go down to the next grade band. If your code is impressively expressive, then your grade will move to the plus side of the level.

_For example, if your submission fulfills the A Level requirements, but your code uses numerous poorly-named variables or functions (like 'x', where 'toggle_value' would provide more information) then that A would drop down to an A-, or perhaps even B+, depending on how egregious things are._

_On the flip side, if your code follows [Python style convention](https://mru-f22-cs1.github.io/content-curtis/extras/python-style.html), uses expressive variable names, is easy to read and well-documented, an A might turn into an A+._

### Citing Sources

If you use any outside resources, make sure you **cite your sources** by including a comment with your source.

**Failure to do so could very well result in a 0 for this assignment, which neither you, nor your instructor, wants.**

As with assignment 2, **you may ONLY use programming structures AND techniques that have been covered in class.** I know it's tempting to do fancy things, but consider it a challenge to stick to the basics.

Finally, citing a source does not give you carte blanche for copying code. If your code significantly duplicates that of another student or an internet resource, it may still be considered academic misconduct.