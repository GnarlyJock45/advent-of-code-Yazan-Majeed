import math

def main():

    count = 0
    dial = 50
    print(f"The dial is now at: {dial}")
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

            cycles = math.floor(int(row[1:]) / 100)

            # To prevent duplicate counting
            is_zero = False

            
            print(f"The dial is rotated: {movement} in the direction of {direction}. The count is: {count} \n")

            print(cycles)
            
            # Deciding the operation based on the direction "L" -> subtract and "R" -> add
            if direction == "L":
                if dial - movement < 0 and cycles == 0:
                    count = count + 1 if dial != 0 else count
                    is_zero = True

                    dial = abs(dial - movement + 100)
                elif cycles > 0:
                    count = count + cycles

                    dial = abs(movement - dial + 100)

                else:
                    dial -= movement

            else:
                if dial + movement > 99 and cycles == 0:
                    count = count + 1 if dial != 0 else count
                    is_zero = True

                    dial = abs(dial + movement - 100)
                elif cycles > 0:
                    count = count + cycles

                    # A new condition added here
                    if dial + movement > 99:
                        count = count + 1 if dial != 0 else count
                        is_zero = True

                    dial = abs(dial + movement - 100)
                else:
                    dial += movement

            count = count + 1 if dial == 0 and not is_zero else count

            print(f"Pointing now at: {dial}")
            
    print(count)


main()