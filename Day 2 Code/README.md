### Problem: Invalid Product IDs
We are given a comma-separated list of product ID ranges (e.g., `11-22`). The goal is to identify and sum all "invalid" product IDs within these ranges. The features of this problem revolve around string pattern recognition. 
The first part requires us to find IDs made up of a sequence of digits repeated exactly twice. The second part takes it further by requiring us to identify IDs made up of a sequence of digits repeated *at least* twice.

### Idea
Instead of mathematically slicing the numbers, we can treat each ID as a string and use Regular Expressions (Regex) to detect the repeating patterns. We parse the ranges, loop through every number within them, check for the pattern, and keep a running sum of the matches.

### Part 1
For this part, an ID is invalid if a sequence repeats exactly two times (e.g., `55`, `123123`). We can identify this using the regex pattern `^(\d+)\1$`. This captures one or more digits `(\d+)` at the start `^` and checks if that exact captured group `\1` repeats once before the end `$` of the string.

### Part 2
The rules expand to include IDs where the sequence repeats two *or more* times (e.g., `111`, `123123123`). We modify our regex to handle this by adding a `+` quantifier to the backreference: `^(\d+)\1+$`. This ensures the captured sequence repeats at least once more, but has no upper limit.

### Intuition
The logic of using regex perfectly handles the problem's core challenge: identifying arbitrary repeating sequences of unknown lengths. Because an ID like `121212` could be seen as `12` repeating three times, regex backreferencing (`\1`) allows the program to dynamically find the base sequence without needing to hardcode substring lengths or write complex integer division logic.

### Approach
* Read the raw input text file.
* Parse the input by splitting at commas, and then at dashes, to create a list of `[start, end]` ranges.
* Initialize a sum variable to 0.
* Loop through each range, generating every ID from the start number to the end number (inclusive).
* Convert the ID to a string and check it against the compiled regex pattern (`^(\d+)\1+$` for Part 2).
* If the ID matches the pattern, add its integer value to the sum.
* Output the final sum.
