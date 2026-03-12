def main():
    sum_dict = {}
    counter = 0
    coordinates_dict = {}
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            line = line.rstrip()
            coordinates_dict[counter] = line.split(",")
            
            
            sum_dict[counter] = int(coordinates_dict[counter][0]) + int(coordinates_dict[counter][1])

            counter += 1

        sorted_dict = sorted(sum_dict.items(), key=lambda item: item[1], reverse=True)
        
        max_val = coordinates_dict[sorted_dict[0][0]]
        min_val = coordinates_dict[sorted_dict[-1][0]]

        area = (int(max_val[0]) - int(min_val[0]) + 1) * (int(max_val[1]) - int(min_val[1]) + 1)
        print(area)

main()