# Problem: ID Ranges Identification
A beam of light starts at "S" and wants to go down, but some splitters are in the way and when a beam hits a splitter it gets split into two (of course it would). Count the **number of splits** as well as the **number of possible outcomes** for a single beam of light - a probability problem

## Idea
After determining where the beam starts, we go down line by line checking if a splitter exists below, then we store the adjacent indices (representing the newly split beam locations).
The main aspect here is storing the locations of each line's beams and using them for the next line.
### Part 1
Going line by line, reading the previous info, updating the line and checking for splitters in the current line. On each splitter **that actually splits an incoming beam** we count up one.
### Part 2
Counting the possible timelines at each beam location, if two splitters create the same beam, then two timelines could be created here, thus the value 2 is stored along the beam's index. This is repeated and each beam's timeline count is incremented till the end, before being summed giving us the total possible timelines for a single beam.

## Intuition
The algorithm in part 2 was hinted by AI, the idea of summing the possible timelines values at each splitter.

## Approach
1. Find the index of the first beam
2. going down, find the indices of current splitters
3. For each splitter, if a beam is directly upwards, create two new beams before ( i - 1) and after it (i + 1) and count up
4. Preserving the locations of previous beams