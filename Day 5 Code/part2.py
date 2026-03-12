def main():
    with open('textFiles/official.txt', 'r') as file:
        lines = file.readlines()

        # Part 1: Splitting the file by the extra newline. The upper part is the ID ranges while the lower one contains the IDs themselves
        id_ranges = [line.strip() for line in lines]


        # This approach is inefficient and doesn't work

        # Part 2: Arranging the ID ranges in list of tuples with "L" and "H" indications
        # We can merge part 2 and 3 to save on memory and compute
        # for id_range in id_ranges:
        #     low, high = id_range.split('-')
        #     final_set.update(range(int(low), int(high) + 1))

        # print(len(final_set))
        

        # New approach: merging ranges and computing the difference between low and high
        id_ranges = [id_range.strip() for id_range in id_ranges]
        id_ranges_lst = []

        for id_range in id_ranges:
            low, high = id_range.split('-')
            id_ranges_lst.append((int(low), int(high)))

        id_ranges_lst.sort()

        merged = []
        current_low, current_high = id_ranges_lst[0][0], id_ranges_lst[0][1]

        for next_low, next_high in id_ranges_lst[1:]:
            if next_low <= current_high + 1:
                current_high = max(current_high, next_high)
            else:
                merged.append((current_low, current_high))
                current_low, current_high = next_low, next_high

        merged.append((current_low, current_high))

            
        total_unique_ids = sum((high - low + 1) for low, high in merged)

        print(total_unique_ids)
                

main()