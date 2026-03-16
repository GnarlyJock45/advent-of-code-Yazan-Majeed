# Problem: Recursive Check
Given a list of inputs and linked outputs, how many distinct paths lead from the input "you" to the output "out"?
Part 2: How many of these paths pass through "dac" and "fft"? 

## Idea
A recursive function that does **Depth-First Search** throughout the inputs -> outputs.
### Part 1
Start where input is "you", loop over its outputs, and repeat till "out" is found in the outputs. Then go back one step and try the other output. Over and over again.
### Part 2
While it seems easy to check for the presence of "dac" and "fft" in the search pipeline, two issues arise: the first is keeping memory when going deeper in the search, the other is related to run time of the program, and thus we have to cache the earlier steps of the depth search.

## Intuition
An external recursive  function gives the needed flexibility in finding the paths, it also is corner-case proof as it tries out all possible paths.

## Approach
1. Create the external `graph(main_dictionary, current_level)` function that loops over the current level's output and checks for the presence of "out"
2. if "out" isn't present, we call the function again and go to the deeper level (if it isn't a dead end) and so on.
3. In part 2, we had to store cache and implement a simple memory for "fft" and "dac" boolean check


A previous try of mine is included below part 2's code as well as a secret message from my younger brother :)