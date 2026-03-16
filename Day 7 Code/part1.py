def main():
    s_idx = ""
    counter = 0
    
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            
            current_splitters = []
            current_beams = []

            if "S" in line:
                for i in range(len(line)):
                    s_idx = i if line[i] == "S" else s_idx

                line = list(line)
                line[s_idx] = "|"
                line = "".join(line)

            else:
                if "^" in line:
                    for i in range(len(line)):
                        if line[i] == "^":
                            if previous_line[i] == "|":
                                current_splitters.append(i)
                                counter += 1


                    # Now we have the splitters of this line (if any), the next step is to actually split and create beams on left and right
                    for i in range(0, len(current_splitters)):
                        line = list(line)
                        line[current_splitters[i] - 1] = "|"
                        line[current_splitters[i] + 1] = "|"
                        line = "".join(line)


                # else:
                    # Enabling modifications on the string
                line = list(line)

                # Preserving the locations of beams from the previous layer
                previous_beams = [i for i in range(len(previous_line)) if previous_line[i] == "|"]
                for i in previous_beams:
                    line[i] = "|" if line[i] != "^" else "^"

                line = "".join(line)

            previous_line = line
            print(line)
        print(f"The count of splits is: {counter}")

main()