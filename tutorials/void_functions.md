# Void Functions

## Tracing
In partners or small groups, work through the following problems **by hand**. How would you check your answers using Python?

1. For the following program:
    ```python
    def test(a: int, b: int, c: int) -> None:
        print(a, b, c)

    def main() -> None:
        a = 1
        b = 2
        c = 3
        test(a, b, c)
        test(b, a, c + 7)

    main()
    ```
    
    Fill in the table below with the values of the parameters `a`, `b`, and `c` *inside* the `test` function for each of the two function calls:

    | Call to `test` | `a` | `b` | `c` |
    | -------------- | --- | --- | --- |
    | First call     |     |     |     |
    | Second call    |     |     |     |

2. Trace the following program. Show the intermediate values assigned to each variable in `main` and `display`, then write the program output.
    ```python
    def display(a: int, b: int) -> None:
        c = 2 * a + b
        print (a, b, c)

    def main() -> None:
        n = 3
        display(5, n)
        display(n, n)
        display(n * n, 12)

    main()
    ```

## Debugging
The following programs do not work. Try to figure out what is wrong by hand first, but you may use VS Code to debug and fix them. 

1. This program should display the hypotenuse of a right-angle triangle, given one angle in degrees and the length of one side.
    ```python
    def hypoteneuse(angle: float, side: float) -> None:
        hyp = side / math.sin(math.radians(angle))
        print(f"The hypoteneuse is {hyp:.2f}.")

    def main() -> None:
        angle = float(input("Enter the angle in degrees: "))
        side = float(input("Enter the length of one side: "))
        hypoteneuse(angle, side)

    main()
    ```

2. This program should greet a person between 1 and 10 times. It uses the `random` module to determine how many times (the use of the `random` module is not the part that is broken).
    ```python
    import random

    def greeting(name: str) -> None:
      n_times = random.randint(1, 10)
      print(f"Hello, {name}! " * n_times)

    def main() -> None:
      name = input("What is your name? ")
      greeting()

    main()
    ``` 

## Function Design
Implement the following problems in a new Python file in VS Code. You'll have to add a `main` function to call and test your new functions.

1. Design a function to compute and display the annual rate of inflation for a given item. The function is passed two prices for the same item: the price one year ago and the price today. The inflation rate should then be displayed as percentage with one decimal place (e.g. 5.3%). 

    One function design strategy is as follows:
    
    1. Ensure you understand the problem.
    2. Develop an *algorithm* to solve the problem.
    3. Write the function definition.
    4. Implement the algorithm in the function body.
    5. Test by calling your function with some test values (e.g. a car that cost $20,000 last year and $23,000 today).

2. Following the same strategy as above, design a function which, given three sides of a triangle $a$ $b$ and $c$, computes and displays the area of the triangle. The area can be calculated using Heron's formula:
    
    $$A = \sqrt{s(s - a)(s - b)(s - c)}$$
    
    where $s$ is the semiperimeter of the triangle:
    
    $$s = \frac{a + b + c}{2}$$