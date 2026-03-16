# Problem: ID Ranges Identification
Based on some given ID ranges, we are tasked with identifying if a certain ID lies in the range or not. This is modified in the second part where we have to count the number of possible IDs from the given range.
The main problem is in two spaces: The first is IDs overlapping, the second is splitting the input correctly (this is easy)
Of course, a big part of it can be brute-forced but this is inefficient, thus I had to do some "manipulation to the ranges in the second part"

## Idea
For each given ID, we loop over the ranges and check if it's higher than the lower range and lower than the higher range, in a nutshell.
### Part 1
I put some effort in arranging and preparing the ranges for comparison, created a list of tuples for the id ranges to ease comparison.
Nested loops were used in part 1 (inefficient) checking each range
### Part 2
Had to merge the overlapping ranges by checking for overlap then removing the "intermediate" ranges, after the loop finished, I did another loop summing the differences between limits (which represents the number of possible IDs)


## Intuition
It is clear and straightforward, a search problem (though I didn't dive deep into the searching algorithms). 
The idea of merging overlapping ids helps in preventing double counting.

## Approach
1. Splitting the file into two parts, the first containing the ranges while the other the ids themselves
2. Splitting the ranges on "-" and storing as low and high limit
3. Looping over the ids, and for each one loop over the ranges till the given id exists in a range.
4. If the given id exists in a range, count up, else continue to the next id.

**Merging:**
1. sorting the id ranges from ascendingly
2. checking if the next low is lower than the current high **AND** the next low is greater than the current high
3. If yes, then remove the "intermediate" low and high and store the extreme ones
4. Repeat
5. Sum up the differences between a range's limits