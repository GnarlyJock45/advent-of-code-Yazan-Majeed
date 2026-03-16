def main():
    sum = 0
    KEEP = 12
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            row = line.strip()

            stack = []
            allowed_drop = len(row) - KEEP

            # Looping over each digit in the numbers string
            for n in row:
                # Checking that the stack is not empty and that we're allowed to drop values. Also that our current value is larger than the top of the stack
                while len(stack) > 0 and allowed_drop > 0 and n > stack[-1]:
                        stack.pop()
                        allowed_drop -= 1

                stack.append(n)
            result = stack[:12]
            
            # Merging the list (stack)
            result = int("".join(result))
            sum += result
        print(f"The sum is: {sum}")                

main()