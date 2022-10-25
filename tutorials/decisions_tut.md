# Decisions
<!-- Note: this is a mash-up of 1501 "Simple Selection" and "Compound Selection" tutorials, with some tweaks, keeping in mind that it follows the "testing and debugging" tutorial. May be a bit too long, but it's right before the midterm, so extra questions are good for practice. -->

## Introduction
This tutorial is intended to get you used to working with simple and compound decisions. In small groups, working on the whiteboard or on paper, work through the following exercises. You can check your answers using the Python interpreter, but try to solve them by hand first.

## Simple decisions
1. Write an **algorithm** that prints `risk` when the value of a variable named `pressure` is above 160, otherwise it prints `no risk`. What test values would you use to ensure your algorithm is correct?
2. Trace the following code segment and write the final value of `result` for the given input values.

    ```python
    result = 10
    total = float(input("Please enter the total: "))
    if total > 100:
        print("Total is", total)
        result = 25
    else:
        print("Total is", total)
        result = 80

    print("Result is", result)
    ```

    | input | result |
    | ----- | ------ |
    | 100   |        |
    | 155   |        |
    | 80    |        |

3. How could the previous program be made simpler without changing its results?

## Complex decisions
Try the following problems **on paper** in order to practice without the help of your IDE.

1. Write a **Python function** that takes 3 integers representing dice rolls as inputs. If all 3 are the same value, return `"3 of a kind!"`. If 2 are the same, return `"A pair!"`. Otherwise, return `"Roll again"`. To check your results, trade answers with another group and trace their code.

    Use the following incomplete program to get you started:
    ```python
    import random

    def roll_results(                              ) -> str:
        """

        """








    def main() -> None:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        result_str = roll_results(a, b, c)
        print(f"You rolled {a}, {b} and {c}. {result_str}")

    main()
    ```
    > How would you test this function to make sure it's working properly?

2. Design an **algorithm** for the following problem:
      The GPA of a student is entered via the keyboard. A message is printed that is dependent on the value of the GPA as shown below.

      | GPA        | Message                                        |
      | ---------- | ---------------------------------------------- |
      | 3.0 to 4.0 | Keep up the great work!                        |
      | 2.0 to 2.9 | Room for improvement, but you're getting there |
      | 1.0 to 1.9 | You're falling behind, is everything okay?     |
      | 0.0 to 0.9 | :(                                             |

      If the user enters a number above 4.0 or below 0.0 display the message `Invalid Input`.

      Which test values would you use to test all possible cases?

3. A mythical country has the following tax structure:

    | Tax rate | No dependents        | Dependents           |
    | -------- | -------------------- | -------------------- |
    | 0%       | Less than \$20,000   | Less than \$40,000   |
    | 10%      | \$20,000 to \$60,000 | \$40,000 to \$60,000 |
    | 20%      | \$60,000 and over    | \$60,000 and over    |

    Write a **Python program** that asks how many dependents the user has and how much money they made, then prints out the amount of tax owing. How would you test whether this program is working correctly?

4. Compare your solution to the previous problem with your neighbours. How many different solutions do see? Can you think of other ways of simplifying your code?