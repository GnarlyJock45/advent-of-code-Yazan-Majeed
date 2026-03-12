def main(): 

    count = 0
    dial = 50
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            row = line.strip() # Removing the newline at the end of each row

            # Values larger than 100 destroy the functionality, so we take the last two digits of the input.
            # If the row has one "tick" then we take the last value, otherwise we take the last two.
            if len(row) == 2:
                movement = int(row[-1:])
            else:
                movement = int(row[-2:])

            direction = row[0]
            
            
            # Deciding the operation based on the direction "L" -> subtract and "R" -> add
            if direction == "L":
                if dial - movement < 0:
                    dial = (dial - movement) + 100
                else:
                    dial -= movement
            else:
                if dial + movement > 99:
                    dial = (dial + movement) - 100
                else:
                    dial += movement

            print(f"The direction is{direction} and the movement is: {movement}. The count is: {count} \n\n")
            count = count + 1 if dial == 0 else count
            print(f"The dial is now at: {dial}")
            
    print(count)


main()