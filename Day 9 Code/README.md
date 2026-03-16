# Problem: Largest Area Rectangle
Given some coordinates, what is the largest area rectangle taking two points as opposite corners?
Part 1 has no constraints, just the largest area rectangle while part 2 requires the proposed rectangle to be completely within the given shape.

## Idea
Computing the sum of each coordiantes and choosing the largest difference ones as largest rectangle. Then finding the area using the known formula.
This idea turned out to be flawed on some corner cases, and so I had to opt for a nested loop check approach. 
### Part 1
Calculating the area of all possible rectangles and choosing the maximum one
### Part 2
I first tried the idea of checking if each corner in the proposed rectangle is covered by 4 red tiles and it didn't work as sometimes in a "U" shape it may appear to be valid when it is not. I resorted to labeling the valid area by a ray-casting method, drawing a straight line between each two neighboring points.   

## Intuition
The working algorithm in part 2 was hinted by AI.
