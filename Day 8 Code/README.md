### Problem: Electrical Junction Box Circuits
We are given a list of 3D coordinates representing electrical junction boxes. Electricity can flow between boxes if they are connected, forming a "circuit." Connections are prioritized by the shortest straight-line distance between pairs.
Part 1 asks us to process the 1000 shortest connections and calculate the product of the sizes of the three largest resulting circuits. Part 2 asks us to continue making connections until every single junction box is part of one unified circuit, and then multiply the X-coordinates of the final pair of boxes that completed the network.

### Idea
This is a classic graph problem (specifically, finding a Minimum Spanning Tree and tracking connected components). The junction boxes are "nodes," and the straight-line distances between them are "edges." By calculating all possible distances, sorting them from shortest to longest, and incrementally linking them, we can simulate the Elves' cabling process.

### Part 1
We represent the initial state as a list of independent sets, where each set contains exactly one box. We iterate through the 1000 shortest edges. If the two boxes for a given edge are in different sets, we merge those sets (representing a connected circuit). Finally, we measure the sizes of all resulting sets, sort them in descending order, and multiply the top three.

### Part 2
Instead of stopping at 1000, we need to find the exact connection that merges the final two disjoint circuits together. To make the merging process slightly more straightforward, we use a simple array where the index is the box and the value is its `circuitID`. When merging, we update all matching IDs to combine the circuits, decrementing our count of isolated circuits until only 1 remains.

### Intuition
Calculating the actual Euclidean distance requires a computationally heavy square root operation. However, because we only care about the *relative* ordering of the distances, we can just use the squared distance `(x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2`. The relative order will remain exactly the same, saving time and avoiding floating-point precision issues. The logic of grouping elements via shared IDs or sets is a simplified implementation of the Disjoint Set Union (DSU) algorithm.

### Approach
* Parse the raw string input into a list of `[X, Y, Z]` integer coordinates.
* Calculate the squared distance for every possible pair of coordinates using nested loops.
* Store these connections in an `edges` list as tuples: `(distance, box_a_index, box_b_index)`.
* Sort the `edges` list in ascending order based on the distance.
* **For Part 1:** Initialize a list of sets. Loop through the first 1000 items in `edges`. If `box_a` and `box_b` belong to different sets, remove the old sets and append their union. Find the lengths of all sets, sort descending, and multiply the top three.
* **For Part 2:** Initialize an array of `circuitID`s from `0` to `n-1`, and set a `remainingCircuits` counter to `n`.
* Loop through the sorted `edges`. If `box_a` and `box_b` have different `circuitID`s, iterate through the ID array and change all instances of `box_b`'s ID to `box_a`'s ID. 
* Decrement `remainingCircuits` by 1. 
* If `remainingCircuits` reaches 1, stop the loop, extract the X-coordinates for `box_a` and `box_b` from the original coordinates list, and return their product.
