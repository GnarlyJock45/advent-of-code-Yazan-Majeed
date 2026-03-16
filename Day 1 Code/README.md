# Problem: Dial Rotation
Given a sequence of rotations, we have to identify the number of time we reach zero. The features of this problem are that it loops around every 100 "ticks" and we have to directions of movement; "L" left and "R" Right.

The first part of the problem requires us to **count the number of** times our rotations stopped at 0 while the second part takes it further by requiring us to determine the number of times we **pass** 0 as well. This proved to be a challenge for values larger than 100 as we have to keep in mind the number of rotations

## Idea
Starting by reading the direction and adding or subtracting based on it.
We then read the magnitude of rotation for each line
### Part 1
We only take the last two digits as the hundreds digit does not affect our counting. We keep count of zeros and that's it
### Part 2
We need to take into consideration larger values and so **Modulo** needs to be used
We calculate how far we are from the next hundred then for each 100 steps, we increase the count once. Finally, we update the dial value via the **remainder**.

## Intuition
The idea of subtracting and addition based on letter is straightforward, as well as counting on reaching 0. However, the second part's modulo and remainder usage splits the problem into two easy steps: counting up based on the number of hundreds and updating based on the last two digits.

## Approach
1. Use string methods to split and read the direction
2. start the dial at 50
3. calculate distance to nearest 100 (sub if "L", add if "R")
4. Use modulo to identify number of hundreds digit
5. Update 