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
