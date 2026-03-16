# Try 1: Flawed Shortcut
# def main():
#     sum_dict = {}
#     counter = 0
#     coordinates_dict = {}
#     with open('textFiles/official.txt', 'r') as file:
#         for line in file:
#             line = line.rstrip()
#             coordinates_dict[counter] = line.split(",")
            
            
#             sum_dict[counter] = int(coordinates_dict[counter][0]) + int(coordinates_dict[counter][1])

#             counter += 1

#         sorted_dict = sorted(sum_dict.items(), key=lambda item: item[1], reverse=True)
        
#         max_val = coordinates_dict[sorted_dict[0][0]]
#         min_val = coordinates_dict[sorted_dict[-1][0]]

#         area = (int(max_val[0]) - int(min_val[0]) + 1) * (int(max_val[1]) - int(min_val[1]) + 1)
#         print(area)

# main()

# Try 2: Brute-Force Systematic Approach
def main():
    coords = []

    # Read the file and parse the coordinates
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                x_str, y_str = line.split(',')
                coords.append((int(x_str), int(y_str)))

    max_area = 0

    # Loop through every unique pair of coordinates
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            # Calculate width and height using absolute difference
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1

            # Calculate area
            area = width * height

            # Update the maximum area if we found a bigger one
            if area > max_area:
                max_area = area

    print(max_area)


main()