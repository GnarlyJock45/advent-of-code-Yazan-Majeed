
def main():
    s_idx = 0
    counter = 0
    total_timeline_counter = []
    previous_timeline_counter = {}
    
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            
            # We build a fresh dictionary for the current row we are looking at
            timeline_counter_dict = {}
            
            if "S" in line:
                for i in range(len(line)):
                    if line[i] == "S":
                        s_idx = i
                # Initialize the starting timeline
                previous_timeline_counter[s_idx] = 1
                
            else:
                # Look at every active "|" index from the previous row
                for idx, count in previous_timeline_counter.items():
                    
                    # If the beam hits a splitter in the CURRENT line
                    if idx < len(line) and line[idx] == "^":
                        # Split left and right: add the previous count to the left index, and the next count to the right index
                        timeline_counter_dict[idx - 1] = timeline_counter_dict.get(idx - 1, 0) + count
                        timeline_counter_dict[idx + 1] = timeline_counter_dict.get(idx + 1, 0) + count
                        
                        # This is the requirement for part 1 of the task, the number of splits
                        counter += 1  # Keeping your counter active for splitters hit
                        
                    else:
                        # No splitter, the beam goes straight down
                        timeline_counter_dict[idx] = timeline_counter_dict.get(idx, 0) + count
                
                # Overwrite the previous one with new data
                previous_timeline_counter = timeline_counter_dict
                
                # Append to history list to track progression throughout
                total_timeline_counter.append(timeline_counter_dict)

    # Calculate the total timelines at the very bottom
    final_sum = sum(previous_timeline_counter.values())
    
    print(f"{counter}")
    print(f"Total timelines at the end: {final_sum}")

main()