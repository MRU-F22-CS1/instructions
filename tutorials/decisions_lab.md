# Decisions
<!-- Note: combo of COMP 1631 and F21 1501 -->

## Part 1: Code analysis
1. Trace the code below and **predict** what the output will be when you run the program. Next, run it. If the output is not what you predicted, try to figure out why.
    ```python
    a = False
    b = True
    c = True

    if a or not b and c:
        print("expression is true")
    else:
        print("expression is false")
    ```

2. Determine how to make the program produce the opposite output by inverting the value of just one variable. Make the change and test to see if you were correct.

3. Next, restore the code to its original form. Can you invert a different variable to achieve the same effect? If so, which one?

## Part 2: Code synthesis
Meal delivery service BypassTheCleaning has hired you to write their app. They offer free delivery for orders of \$40 or more, and they want your app to display the amount remaining to get free delivery.

1. **Design** a program that prompts the user for the dollar amount of their current order, then prints out a message according to the following table:

    | Amount                   | Message                                         |
    | ------------------------ | ----------------------------------------------- |
    | amount $\lt 0$           | `Invalid entry, orders must be positive`        |
    | $0 \leq$ amount $\lt 40$ | `Add $xx.xx to your order to get free delivery` |
    | $40 \leq$ amount         | `You get free delivery!`                        |
    
    Your program should have a `main` function as well as at least one other function. You can assume the user input data type is always correct (e.g. a number will be entered when it is expected by the program).

    You may use the following template as a guide, but feel free to get creative:
    ```python
    def check_free_delivery(              ) -> None:
        """

        """





    def main() -> None:
        ""
    
    main()
    ```

    The program should look like the following when run, where 25.30 is an examples of user input.

    <pre>
    What is the dollar amount of the current order? <span style="font-style: italic; font-weight: bold;">25.30</span>
    Add $14.70 to your order to get free delivery</pre>

    Note that by default, Python will not print out exactly two decimal places. This is a good chance to practice your [f-string](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) skills.

2. **Implement** the program from step 1. Is there anything you forgot during the design stage?
   > One of your variables should be defined as a **constant**. Which one?
3. **Test** the program. What test values should you use to make sure you know it is completely working?

## Bonus challenge
In Part 2, you wrote a program to check if a user gets free delivery based on their order amount. Now, BypassTheCleaning wants you to make sure that only users within **20 km** get free delivery. Modify the previous program to prompt the user for their delivery distance, then print messages according to the following table:

| Distance                   | Message                                         |
| -------------------------- | ----------------------------------------------- |
| distance $\lt 0$           | `Invalid entry, distance must be positive`      |
| $0 \leq$ distance $\lt 20$ | Proceed to check amount                         |
| $20 \leq$ distance         | `Sorry, you are not eligible for free delivery` |
