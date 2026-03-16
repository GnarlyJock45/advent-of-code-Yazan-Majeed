def main():
    # For this one we need to go recursive

    main_dict = {}
    with open('textFiles/official.txt', 'r') as file:
        # Step 1: Map the info to a dictionary
        for line in file:
            line = line.strip()

            text_in, text_out = line.split(":")
            text_out = text_out.split(" ")[1:]
            main_dict[text_in] = text_out

        
        counter = graph(main_dict=main_dict, current_level=main_dict['you'])
        
        print(f"The counter is: {counter}")

# Step 2: Define a recursive function that listens for value == "out"
def graph(main_dict, current_level):

    counter = 0

    for value in current_level:
        if value == "out":
            counter += 1
            break
        elif main_dict[value] :
            current_level = main_dict[value]
            counter += graph(main_dict, current_level)

    return counter

main()