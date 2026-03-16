def main():

    split_idx = 0
    count = 0
    
    with open('textFiles/official.txt', 'r') as file:
        lines = file.readlines()

        # Part 1: Splitting the file by the extra newline. The upper part is the ID ranges while the lower one contains the IDs themselves
        split_idx = [idx for idx, line in enumerate(lines) if line == "\n"][0]

        id_ranges = lines[0: split_idx]
        id_ranges = [id_range.strip() for id_range in id_ranges]

        ids = lines[split_idx + 1: ]
        ids = [id.strip() for id in ids]


        # Part 2: Arranging the ID ranges in list of tuples with "L" and "H" indications
        id_ranges_lst = []

        for id_range in id_ranges:
            low, high = id_range.split('-')
            id_ranges_lst.append((low, high))

        # Part 3: Checking if it fits then count up
        for n in ids:
            n = int(n)
            for i in range(0, len(id_ranges_lst)):
                current_range = (int(id_ranges_lst[i][0]), int(id_ranges_lst[i][1]))
                if  n >= current_range[0] and n <= current_range[1]:
                    print(f"{n} is higher than {current_range[0]} and less than {current_range[1]}")
                    count += 1
                    break

        print(f"The count is: {count}")

main()