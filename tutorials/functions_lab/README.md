# Functions

## Part 1: Tracing and debugging
You and a friend are developing a journalling app to keep track of your hiking adventures. Your friend started writing the code, so you decide to read what they've got so far to make sure you understand how it works.

1. Download and open [hiking_journal.py](https://raw.githubusercontent.com/MRU-F22-CS1/instructions/main/tutorials/functions_lab/hiking_journal.py)
2. Trace the code **manually** and write down your predicted output.
3. Run the code. Did it produce what you expected?
4. Try changing the function call to `journal_entry(10.5, "July 12, 2022", "I saw a beautiful lake.")`. What happens?
5. Add an indentation (4 spaces, or tab) before the `main()` statement in the last line of the script. What happens? 
6. Undo your changes so that the file is back to the original.
7. **Without modifying the `journal_entry` function**, change the code so that the journal entry is printed to the screen.

## Part 2: Writing functions
In this exercise, you will use Python's random number generator to implement a simple dice game. The score for each player is calculated by rolling two dice and adding them together, then either adding, subtracting, or ignoring the length of their name. 

1. Download and open [game.py](https://raw.githubusercontent.com/MRU-F22-CS1/instructions/main/tutorials/functions_lab/game.py). At the very top, you'll see this line:
   
   ```python
   from random import randint
   ```
   This makes the `randint` function available to use in this script.

   > This is a different type of import than you've seen so far - instead of importing the entire `random` module, we're just importing the `randint` function. By doing this we don't need to type `random.randint` to call the function.

2. The script defines three **functions**:
   - `roll_dice`: uses `randint` to virtually roll two dice and add them together. This function is complete, you don't need to make any changes to it.
   - `play_game`: an int-returning function that takes one **argument**, `name` (a string). This is where you will be implementing the game logic.
   - `main`: a void function that serves as the entry point into the program. This is where you will prompt the user for input and call the `play_game` function.
3. In `main`, implement following algorithm:
   
   ```plaintext
   1. Prompt the user to enter the name of player 1
   2. Prompt the user to enter the name of player 2
   3. Call play_game to calculate the score of player 1
   4. Call play_game to calculate the score of player 2
   5. Display the score of both players.
   ```
   
   > You may define additional functions if you like, the main goal is to get used to calling functions and returning values.

4. In `play_game`, implement the game logic as follows:

   ```python
   score = roll_dice() + weight * len(name)
   ```
   where `weight` is a random integer equalling -1, 0, or 1.
   > Hint: check out the [Python docs](https://docs.python.org/3/library/random.html#random.randint) for how to use the `randint` function to assign the `weight` value.

5. Finally, print out each player's name and their score as an integer.

Your game should look something like the following when run:

<pre class="sample">
Enter the name of player 1: <span style="color: green;">Cali</span>
Enter the name of player 2: <span style="color: green;">Salvador</span>
Cali scores 6!
Salvador scores 11!</pre>

Feel free to get creative with the wording and output formatting, as long as the score is displayed as an integer. You could even add some Unicode symbols for fun, such as:

<pre class="sample">
🎉 Cali scores 6!
🎉 Salvador scores 11!</pre>