### Problem: Cephalopod Math Homework
We are given a worksheet of math problems formatted as a large text grid. The grid consists of numbers and operators (`+` or `*`). The problems are organized into blocks separated by completely blank columns. 
The first part requires us to read horizontal numbers within a block and apply the operator found at the bottom of the block to all of those numbers. The second part introduces a twist: cephalopod math is actually read vertically. Each column forms a single number (read top-to-bottom), and we must apply the block's operator to these vertical numbers. The final goal for both parts is to find the grand total of all the evaluated blocks.

### Idea
Instead of parsing the input line-by-line as standard text, we can map the entire input into a 2D matrix of characters. This allows us to traverse the data column-by-column rather than row-by-row. By keeping track of empty columns, we can identify when one math problem ends and the next begins.

### Part 1
For the first part, the numbers are arranged horizontally. The approach involves grouping the numbers within a block, parsing them into integers, and applying the operator located in the final row of that block. (Note: The provided Part 1 code uses a hardcoded row-index approach, which works if the input strictly has exactly 4 rows of numbers before the operator).

### Part 2
The rules change drastically here: each column represents a number, with the top digit being the most significant. Even though the problem states problems are read right-to-left, addition and multiplication are commutative. Therefore, reading the columns left-to-right within a block yields the exact same mathematical result. We scan top-to-bottom to build the integer, and check the bottom row for the operator.

### Intuition
Treating the text as a coordinate grid makes column-based reading trivial. Furthermore, using ASCII integer values directly (`ord(char)`) is a highly efficient way to build numbers. Instead of concatenating characters into a string and parsing it (e.g., `'6' + '2' + '3' = '623'`), we can mathematically shift the value by multiplying by 10 and adding the new digit (`v = v * 10 + (charVal - 48)`). Spaces (ASCII `32`) naturally serve as our filters for empty space and block delimiters.

### Approach
* Parse the raw string into a 2D matrix of characters, splitting by newlines.
* Determine the maximum column length among all rows to ensure we iterate through the entire width of the worksheet.
* Initialize variables for the grand `answer`, the current `blockTotal`, and the current operator (defaulting to `+`, ASCII 43).
* Iterate through the matrix column-by-column (`for i in range(maxDigits)`).
* For each column, iterate top-to-bottom through the rows (excluding the last row). If a character is not a space, convert it to a digit and build the column's number mathematically.
* Check the final row of the current column to see if an operator exists. If so, update the block's operator.
* If the column contained digits, apply the operator to the running `blockTotal`.
* If the column was entirely empty (no digits and no operators), it signifies the end of a block. Add the `blockTotal` to the grand `answer`, and reset the `blockTotal` and operator for the next block.
* Return the grand total once all columns are processed.
