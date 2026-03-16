### Problem: Forklift Paper Roll Optimization
We are given a 2D grid representing a room filled with large rolls of paper (`@`) and empty spaces (`.`). The Elves' forklifts can only access a roll of paper if it has fewer than four other rolls in its eight adjacent neighboring positions (horizontal, vertical, and diagonal). 
The first part of the problem asks us to count how many paper rolls are initially accessible. The second part introduces a chain reaction: removing accessible rolls frees up space, potentially making deeper rolls accessible. We need to find the total number of paper rolls that can be removed if we repeatedly clear out accessible rolls in simultaneous waves until no more can be reached.

### Idea
We can represent the layout as a 2D matrix (list of lists). By defining the eight directional offsets (`[-1, 0], [1, 1]`, etc.), we can easily check the boundaries and count the neighboring `@` symbols for any given coordinate to determine if a roll is accessible.

### Part 1
For the first part, we perform a single pass over the entire matrix. For every cell containing a paper roll (`@`), we count the number of surrounding `@`s. If the count is strictly less than 4, we increment our "accessible" counter. No modifications to the grid are needed here.

### Part 2
The second part introduces a state-change loop similar to a cellular automaton. The critical requirement is that removals must happen in distinct "passes" or "waves." We cannot alter the grid *while* we are checking it, as doing so would prematurely change the neighbor counts for adjacent cells in the same pass. Instead, we scan the grid, record the coordinates of all accessible rolls in a temporary list, and only turn them into empty spaces (`.`) after the entire grid has been scanned. We repeat this process in a `while` loop until a pass results in zero removals.

### Intuition
The core insight is recognizing the difference between sequential updates and simultaneous updates. In Part 2, isolating the "evaluation" phase from the "mutation" phase prevents a cascade of incorrect deletions during a single pass. By keeping track of a `toRemove` list, we preserve the grid's state for accurate neighbor evaluation, seamlessly splitting the problem into identifying targets and updating the map.

### Approach
* Read the input text and parse it into a 2D matrix using `splitlines()` and list comprehension.
* Define a helper function `canAccess` that uses an array of coordinate offsets to check all 8 neighboring cells, being careful to check grid boundaries to avoid `IndexError`.
* **For Part 1:** Iterate through the matrix, using `canAccess` on every `@`, and sum up the `True` results.
* **For Part 2:** Create a `while` loop that continues as long as `canBeAltered` is True.
* Inside the loop, do a full scan of the matrix. If a roll `canAccess` evaluates to True, append its `(row, col)` tuple to a `toRemove` list.
* After the scan finishes, iterate through the `toRemove` list and change those specific matrix coordinates to `.`.
* Add the length of `toRemove` to a total counter. If the list is empty, exit the loop and return the total removed.
