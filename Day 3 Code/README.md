# Problem: Largest Combination
Given a string of integers, find the largest combination preserving order. It seems easy at first, but the order preservation is difficult, especially in part 2. It requires us to loop over the values and can easily be done by brute forcing the loops, though this is inefficient.

## Idea
The key idea is in determining the largest values and arranging them is different between the parts:
### Part 1
The goal is to get the largest combination of two integers, we start by looping to find the largest value, it will always be included in the final return. After that, we loop over the values and those to the left of the largest are assigned to the tens digit, while those on the right are assigned to the ones digit. Finally, we choose the highest value, as simple as that.
## Part 2
Things are harder now as we need to return the 12 largest values and discard the rest. Here we implement a stack (LI-FO) by storing each value in the loop with a while condition stating that if the next value in the string is larger than the top of our stack, we "pop" the latter, even if more than one value satisfies this condition, it goes on till the value in the string is not larger than the stack's top.

## Intuition
The first part's idea works by storing the index of the largest value and utilizing the understanding of digits as well as handling strings.
The second part's idea (mainly the stack) was hinted by AI, it allows our code to be flexible and cover all corner cases

## Approach
1. Loop over each line in the file
2. Loop over each character (transform it to int) in the line
3. if the value is larger than the stack's top (starts at 0 so it definitely initiates), we remove the stack's head and check again
4. If the while loop is done, we add the new value to the head of the list