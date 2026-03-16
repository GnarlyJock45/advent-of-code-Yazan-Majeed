def main(): 
    sum = 0
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            row = line.strip()

            # Setting the variables to reset with every new line
            largest = 0
            largest_index = 0
            comb_list = []

            # Using enumerate to get the index and value of each item in the list
            for idx, n in enumerate(row):
                n = int(n)

                # Storing the maximum value over the entire list as well as its index (used for getting the largest two digits later on)
                if n > largest:
                    largest = n
                    largest_index = idx
            

            # For items to the left of the largest value, they will be in the tens digit and the largest in the ones
            for idx, n in enumerate(row):
                if idx < largest_index:
                    value = f"{n}{largest}"
                    comb_list.append(int(value))

                # For items to the right of the largest value, they will be in the ones digit while the largest in the tens
                elif idx > largest_index:
                    value = f"{largest}{n}"
                    comb_list.append(int(value))

            sum += max(comb_list)
        print(f"The sum is: {sum}") 
                

main()