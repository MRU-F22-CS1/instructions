# some expected results

Here are a few of the buildings used in the tool we're using to test your applications. For each building, there is also the expected `scoring-results.txt` file so you can check your work.

None of these files should cause your application to explode - if you don't have wood or stone scoring implemented, you can put a 0 in for those scores, or even a blank. Just don't go boom!

Just to be clear: to get a C, your `scoring-results.txt` contents do NOT have to match the report - just the SCORES for glass and recycled have to match. **Make sure you have the word `glass` and `recycled` on the lines you report those scores, though!**

## Explanations: aka why these particular buildings were provided

`c-level-test-1.txt`

> Containing only Recycled and Glass dice
> Be sure you count Recycled dice on all rows **and** all columns
> **and** both stone and wood scores are zero

---

`c-level-test-2.txt`

> Tricky, like the previous building but now the Recycled dice are in the last column and bottom row.
> Be sure to tally the number of Recycled dice from all locations in the building.

---

`b-level-test-1.txt`

> Only two rows? 
> Wood and Stone are zeros!

---

`b-level-test-2.txt`

> With Glass dice on mutiple rows, we'll need to total up a row **and** then add all the rows for the ultimate Glass score.

---

`stone-test-1.txt`

> Stone in multiple levels; recall, 8 points for a Stone die on the 4th (or higher) level of the building.

