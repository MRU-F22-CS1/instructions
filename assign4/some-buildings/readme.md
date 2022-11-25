# Some Buildings

Heya.

I've put a few building files you can use to test your app in this folder. I've added some comments, too. Maybe you'll find them useful.

## Possible Arrangements

There are 28 possible arrangements of 6 dice into 3 stacks. It'd be useful to think about what they are; here are some hints:

- there are 3 buildings consisting of a single stack
- there are 15 buildings consisting of 2 stacks
- there are 10 buildings consisting of 3 stacks


## glass-0-6-0

You'll probably want to test your app with buildings that have **every** dice in the building one particular material. I like this building because it uses all 6 possible numbers, is the maximum height you can possibly have, and has emptiness on both sides of the dice.

## wood-5-0-1

Wood's pretty tricky. I'd definitely suggest seeing how your scoring behave when a wood die doesn't have **any** neighbours. Poor thing.

## rec-1-1-4

It'd be good to make sure recycled dice aren't using the numbers at all, or are being scored row-by-row. This building should take care of checking that...

## stone-1-5-0

Stone gets a bit weird once it hits the 4th level and up. Better make sure that's working. Plus having a blank column on the right might cause some grief. Maybe.