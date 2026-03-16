def main():
    with open('textFiles/official.txt', 'r') as file:
        lines = file.readlines()

        
        id_ranges = [line.strip() for line in lines]


        # This approach is inefficient and doesn't work
        
        # for id_range in id_ranges:
        #     low, high = id_range.split('-')
        #     final_set.update(range(int(low), int(high) + 1))
        # print(len(final_set))
        

        # New approach: merging ranges and computing the difference between low and high
        id_ranges = [id_range.strip() for id_range in id_ranges]
        id_ranges_lst = []

        # A list of tuples containing (lower_limit, upper_limit)
        for id_range in id_ranges:
            low, high = id_range.split('-')
            id_ranges_lst.append((int(low), int(high)))

        # Sorting is needed to check for overlap
        id_ranges_lst.sort()

        merged = []
        current_low, current_high = id_ranges_lst[0][0], id_ranges_lst[0][1]

        # looping over the "next range" to check for overlap
        for next_low, next_high in id_ranges_lst[1:]:
            if next_low <= current_high + 1:
                current_high = max(current_high, next_high)
            else:
                merged.append((current_low, current_high))
                current_low, current_high = next_low, next_high

        merged.append((current_low, current_high))

        # Summing the differences between the limits of each range
        total_unique_ids = sum((high - low + 1) for low, high in merged)

        print(total_unique_ids)
            
main()