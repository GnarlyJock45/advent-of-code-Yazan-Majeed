def main():
    main_dict = {}
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            line = line.strip()
            text_in, text_out = line.split(":")
            text_out = text_out.split(" ")[1:]
            main_dict[text_in] = text_out

    # Create an empty dictionary to store our cached answers
    cache = {}
    
    # We pass 'svr' as a single string
    counter = graph(main_dict, "svr", False, False, cache)
    print(f"The counter is: {counter}")


def graph(main_dict, current_node, fft, dac, memo):
    # 1. Update flags for the device we are currently looking at
    if current_node == "fft": fft = True
    if current_node == "dac": dac = True

    # 2. Check the Cache - This is the main new addition over the previous try
    # Our unique state is where we are, and what we've seen.
    state = (current_node, fft, dac)
    if state in memo:
        return memo[state] # We already calculated this Return it instantly.

    # 3. Reached the end?
    if current_node == "out":
        return 1 if (fft and dac) else 0

    counter = 0
    
    # 4. Loop through the next devices and add up their paths
    if current_node in main_dict:
        for next_node in main_dict[current_node]:
            # Pass the individual next_node down the chain
            counter += graph(main_dict, next_node, fft, dac, memo)

    # 5. Save the final answer to the cache before we return it so we never have to calculate it again
    memo[state] = counter
    
    return counter

main()


# A message from my younger brother, Ibrahim:
# print("i love yazan so mutch -_-   (:")

# for i in range(len.__annotate__(vars)[3] ):
#     PendingDeprecationWarning.add_note
#     i = g = True for i in main : if f == 50 print("hi ") elif range(license.hasattr(print(h[assert, finally{hasattr.await("bro[BrokenPipeError]".BrokenPipeError[assert(yield)range([and{you.except(23.await(you_-)([iter.issubclass[adhsf,.__spec__.__spec__.eval(if car == "HI BRO " print(notgoodtasarfyou are juhsh.ArithmeticError([{hiuhuhjioj(f=0 g)}])))]]))}])])}])))




# First try, it worked well but was so inefficient as it has no "memory"
# def main():

#     # For this one we need to go recursive

#     main_dict = {}
#     with open('textFiles/official.txt', 'r') as file:
#         # Part 1: Map the info to a dictionary
#         for line in file:
#             line = line.strip()

#             text_in, text_out = line.split(":")
#             text_out = text_out.split(" ")[1:]
#             main_dict[text_in] = text_out

#         counter = graph(main_dict=main_dict, current_level=main_dict['svr'])
        
#         print(f"The counter is: {counter}")


# def graph(main_dict, current_level, fft=False, dac=False):

#     counter = 0
    
#     for value in current_level:
#         if value == "out":
#             if fft and dac:
#                 counter += 1
#             # break
#         elif value in main_dict:
#             next_fft = True if value == "fft" else fft
#             next_dac = True if value == "dac" else dac
#             # current_level = main_dict[value]
#             counter += graph(main_dict, main_dict[value], next_fft, next_dac)
#             print(f"we are at level: {value}:{main_dict[value]}")

#     return counter

# main()