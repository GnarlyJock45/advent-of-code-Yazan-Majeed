def main():
    count = 0
    dial = 50
    print(f"The dial is now at: {dial}")
    
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            row = line.strip()


            direction = row[0]
            # Grab the full distance, no matter how many digits it has (on part 1, I took the last two digits but it doesn't work here)
            distance = int(row[1:]) 

            # 1. Calculate steps needed to hit 0 the FIRST time 
            if direction == "L":
                dist_to_first_zero = dial if dial != 0 else 100
            else: # "R"
                dist_to_first_zero = 100 - dial if dial != 0 else 100

            # 2. If we travel far enough to hit 0, calculate total hits
            if distance >= dist_to_first_zero:
                # We hit it once, plus 1 for every full 100 steps left over
                count += 1 + (distance - dist_to_first_zero) // 100

            # 3. Safely update the dial's final position using Modulo math
            if direction == "L":
                dial = (dial - distance) % 100
            else:
                dial = (dial + distance) % 100

            print(f"Rotated  {row}. Count is now:  {count}. Dial resting at:  {dial}")
            
    print(f"Final Password Count: {count}")

main()
