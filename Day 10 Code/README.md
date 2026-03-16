### Problem: Factory Machine Initialization
We are tasked with configuring a series of factory machines using a set of buttons. 
In Part 1, we must match a specific pattern of indicator lights (on/off). Each button toggles a specific set of lights, and we need to find the minimum number of button presses to achieve the target configuration starting from an all-off state. 
Part 2, however, is an absolute nightmare of a difficulty spike. The indicator lights are replaced by joltage counters that scale upwards infinitely. Pressing a button now increments the values of its associated counters by 1. We must find the minimum total button presses to reach an exact sequence of target integers, turning a standard puzzle into a brutal mathematical wall.

### Idea
Because Part 1 involves a relatively small state space of binary toggles, it can be easily solved using a standard Breadth-First Search (BFS). Part 2 is a massive trap. Brute-forcing it will literally run forever because the combinations of integer additions are practically infinite. To survive Part 2, we have to abandon traditional pathfinding entirely, bring in the heavy artillery, and model it as an Integer Linear Programming (ILP) problem so a mathematical solver can do the impossible.

### Part 1
We represent the on/off state of the lights as a `frozenset` containing the indices of the lights that are currently "on". Pressing a button is equivalent to applying a symmetric difference (XOR operation, `^`) between the current state set and the button's toggle set. We use a queue to perform a BFS, keeping track of visited states to avoid loops, guaranteeing the first time we reach the target state is via the absolute minimum number of presses.

### Part 2
Since brute force is a dead end, we treat the number of times each button is pressed as an unknown integer variable. This forms a massive system of linear equations: $Ax = b$, where $A$ is a matrix representing which counters each button affects, $x$ is the vector of button presses (our variables), and $b$ is the target joltage vector. Our objective is to minimize the total sum of presses. We feed this beast into `scipy.optimize.linprog` with strict integrality constraints to solve it.

### Intuition
BFS is naturally suited for Part 1 because it gently explores all binary states step-by-step. For Part 2, a search algorithm is a death sentence; you can press buttons endlessly, meaning there is no bottom to the search tree. Formulating it as an ILP problem completely shifts the paradigm from combinatorial exploration—which would take until the heat death of the universe—to mathematical optimization, instantly finding the exact minimum in a fraction of a second.

### Approach
* Parse the input to extract the initial target sequence and the wiring schematic for each button.
* **For Part 1:** Initialize a `deque` with the starting state (an empty `frozenset`) and 0 presses.
* Dequeue a state, check if it matches the target. If not, apply every button's toggle logic using set XOR, and enqueue any unvisited new states with `presses + 1`.
* **For Part 2:** Construct an equality matrix (`A_eq`) where columns are buttons and rows are counters. Populate it with 1s where a button affects a counter.
* Set the objective function array (`c`) to all 1s, as we want to minimize the total sum of presses.
* Set the bounds for all variables to `(0, None)` to prevent negative button presses, and enforce integrality so the solver only returns whole-number presses.
* Add a `tqdm` loading bar (because waiting for even the optimized math to finish is agonizing), pass these parameters into `linprog` using the `'highs'` method, and extract the minimized objective value.
