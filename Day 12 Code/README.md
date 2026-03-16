### Problem: Present Packing (2D Bin Packing)
We are stuck in a cavern trying to help Elves pack oddly-shaped presents (polyominoes/Tetris pieces) under Christmas trees. We are given a list of standard present shapes and a list of target regions defined by their width and height ($W \times H$). Each region also dictates exactly how many of each shape must be packed into it. 
Presents can be rotated and flipped, but they must align perfectly with the grid and cannot overlap. The goal is to determine exactly how many of the given regions can successfully fit all of their assigned presents.

### Idea
This is a classic "Exact Cover" or 2D bin packing problem. Because the combinations of placements are astronomically high, brute-forcing a 2D array placement step-by-step is too slow. Instead, we can precompute all valid orientations and positions for every piece as 1D integer bitmasks, and then use a Depth First Search (DFS) with backtracking to try and combine these masks.

### Part 1
The core challenge is generating the geometries. We must take the raw `#` and `.` ASCII shapes, convert them to `(row, col)` coordinates, and systematically apply matrix transformations to generate all 8 possible orientations (4 rotations $\times$ 2 flips). Once normalized, we slide these shapes across the target grid, discarding any placements that go out of bounds, and save the valid ones.

### Part 2
*(Note: Since only the Part 1 code and problem statement were provided, this logic reflects the heavy exact cover algorithm required to solve the packing aspect of the puzzle. If Part 2 introduces a new twist, like infinite grids or 3D packing, the bitmasking approach will need a serious overhaul!)*

### Intuition
Why use bitmasks instead of a 2D list or matrix? A grid like $12 \times 5$ has 60 cells. This fits perfectly inside a standard 64-bit integer. By mapping 2D coordinates to a 1D bit shift (`1 << (row * width + col)`), an entire grid state becomes a single number. 
Checking if two pieces overlap, which normally takes nested loops, becomes a single CPU instruction: bitwise AND (`boardMask & m == 0`). Placing a piece is just a bitwise OR (`boardMask | m`). This optimization is the only reason the DFS finishes before next Christmas. Sorting the tasks by the most constrained pieces (fewest valid moves) further trims the massive recursive search tree.

### Approach
* Parse the input to separate the shape definitions from the region requirements.
* Create a helper function `getOrientations` that applies coordinate multipliers (`1` or `-1`) and transpositions (`True` or `False`) to generate all rotated and flipped coordinate sets for a given shape.
* Normalize these coordinates so the top-leftmost point is always at $(0, 0)$ to easily slide them across the board and eliminate duplicates using a `set`.
* For each region, calculate the total area of the required shapes. If it exceeds $W \times H$, instantly return `False` to save time.
* Precompute every valid placement for every required shape on the specific grid, converting each valid placement into an integer bitmask.
* Sort the shapes based on how many valid masks they have, prioritizing the pieces with the fewest options to fail as early as possible.
* Execute a recursive DFS: check if the current piece's mask overlaps the `boardMask` using `&`. If it's clear, combine them using `|` and recurse to the next piece. If it hits a dead end, backtrack and try the next mask.
* Wrap the region loop in a `tqdm` loading bar to preserve your sanity, and tally up the successful fits.
