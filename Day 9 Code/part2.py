def main():
    # 1. Read vertices from the file
    # The file contains the coordinates of the red tiles in order, forming an orthogonal polygon
    vertices = []
    with open('textFiles/official.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                vertices.append((x, y))
    
    if not vertices:
        print("No data found.")
        return
        
    n = len(vertices)
    
    # 2. Extract the boundary edges connecting the red tiles
    edges = []
    for i in range(n):
        edges.append((vertices[i], vertices[(i + 1) % n]))
        
    # Helper Function: Ray-casting to check if a point is strictly inside the green area
    def is_point_inside(Tx, Ty):
        # Check if the point is sitting directly on a polygon edge
        for (ex1, ey1), (ex2, ey2) in edges:
            if ey1 == ey2 == Ty and min(ex1, ex2) <= Tx <= max(ex1, ex2):
                return True
            if ex1 == ex2 == Tx and min(ey1, ey2) <= Ty <= max(ey1, ey2):
                return True
        
        # Cast a ray to the right (+x) and count vertical edge intersections
        intersects = 0
        for (ex1, ey1), (ex2, ey2) in edges:
            if ex1 == ex2: # Vertical edge
                if ex1 > Tx: # Edge is to the right
                    # Check if the ray passes horizontally through the vertical segment
                    if min(ey1, ey2) <= Ty < max(ey1, ey2):
                        intersects += 1
        
        # Odd number of intersections means the point is inside
        return intersects % 2 == 1

    # 3. Generate all pairs of vertices and calculate their areas
    pairs = []
    for i in range(n):
        for j in range(i, n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            pairs.append((area, x1, y1, x2, y2))
            
    # Sort pairs by area in descending order
    # This allows us to exit as soon as we find the first valid rectangle!
    pairs.sort(key=lambda item: item[0], reverse=True)
    
    # 4. Validate rectangles starting from the largest
    for area, x1, y1, x2, y2 in pairs:
        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        
        valid = True
        
        # --- Check A: Ensure no other red tile (vertex) is trapped strictly inside ---
        for vx, vy in vertices:
            if xmin < vx < xmax and ymin < vy < ymax:
                valid = False
                break
        if not valid: continue
        
        # --- Check B: Ensure no boundary edge cuts straight through the rectangle ---
        for (ex1, ey1), (ex2, ey2) in edges:
            if ey1 == ey2: # Horizontal edge
                if ymin < ey1 < ymax and min(ex1, ex2) <= xmin and max(ex1, ex2) >= xmax:
                    valid = False
                    break
            else: # Vertical edge
                if xmin < ex1 < xmax and min(ey1, ey2) <= ymin and max(ey1, ey2) >= ymax:
                    valid = False
                    break
        if not valid: continue
        
        # --- Check C: Dimensional checks and center point verification ---
        if xmin == xmax and ymin == ymax:
            # It's a single 1x1 tile on a vertex. It is inherently valid.
            pass 
            
        elif xmin == xmax:
            # It's a 1D vertical line
            # Check for vertices perfectly blocking the line
            for vx, vy in vertices:
                if vx == xmin and ymin < vy < ymax:
                    valid = False
                    break
            if not valid: continue
            
            # Check for horizontal edges crossing the line
            for (ex1, ey1), (ex2, ey2) in edges:
                if ey1 == ey2 and ymin < ey1 < ymax and min(ex1, ex2) < xmin < max(ex1, ex2):
                    valid = False
                    break
            if not valid: continue
            
            # Ensure the midpoint of the line is inside the polygon
            if not is_point_inside(xmin, ymin + 0.5):
                valid = False
                
        elif ymin == ymax:
            # It's a 1D horizontal line
            # Check for vertices perfectly blocking the line
            for vx, vy in vertices:
                if vy == ymin and xmin < vx < xmax:
                    valid = False
                    break
            if not valid: continue
            
            # Check for vertical edges crossing the line
            for (ex1, ey1), (ex2, ey2) in edges:
                if ex1 == ex2 and xmin < ex1 < xmax and min(ey1, ey2) < ymin < max(ey1, ey2):
                    valid = False
                    break
            if not valid: continue
            
            # Ensure the midpoint of the line is inside the polygon
            if not is_point_inside(xmin + 0.5, ymin):
                valid = False
                
        else:
            # It's a standard 2D rectangle
            # Pick a test point strictly inside the rectangle to ensure it isn't completely outside
            if not is_point_inside(xmin + 0.5, ymin + 0.5):
                valid = False
                
        # If the rectangle survived all checks, it's valid!
        # Because we sorted by area descending, the first valid one is the maximum.
        if valid:
            print(f"Largest Area: {area}")
            return

main()

# The below code represents my first try in this problem, unfortunately it is wrong

# def main():
#     sum_dict = {}
#     counter = 0
#     coordinates_dict = {}
#     data = []
#     with open('textFiles/official.txt', 'r') as file:
#         for line in file:
#             line = line.rstrip()
#             coordinates_dict[counter] = line.split(",")
            
            
#             sum_dict[counter] = int(coordinates_dict[counter][0]) + int(coordinates_dict[counter][1])

#             # ---- Taking the data to sort it later (for part 2)
#             data.append((int(coordinates_dict[counter][0]), int(coordinates_dict[counter][1])))

#             counter += 1

#         sorted_dict = sorted(sum_dict.items(), key=lambda item: item[1], reverse=True)
        
#         max_val = coordinates_dict[sorted_dict[0][0]]
#         min_val = coordinates_dict[sorted_dict[-1][0]]
#         min_val[0], min_val[1], max_val[0], max_val[1] = int(min_val[0]), int(min_val[1]), int(max_val[0]), int(max_val[1])

#         area = (max_val[0] - min_val[0] + 1) * (max_val[1]- min_val[1] + 1)

#         # --------- Part 2 ---------

#         # Step 1: Generate the other 2 corners
#         bottom_left = (min_val[0], max_val[1])
#         top_right = (max_val[0], min_val[1])
#         # Now we have the four corners: min_val -> top left, top_right, bottom_left, max_val -> bottom right

#         # Step 3: Apply a for loop on all possible rectangles
#         # This idea will be used again iteratively
#         sorted_dict = sorted(sum_dict.items(), key=lambda item: item[1], reverse=True)
        
#         area = 0
#         for i in range(len(sorted_dict)):
#             for j in range(0, len(sorted_dict) - i):
#                 max_val = coordinates_dict[sorted_dict[i][0]]
#                 min_val = coordinates_dict[sorted_dict[len(sorted_dict) - j - 1][0]]
#                 min_val[0], min_val[1], max_val[0], max_val[1] = int(min_val[0]), int(min_val[1]), int(max_val[0]), int(max_val[1])

#                 bottom_left = (min_val[0], max_val[1])
#                 top_right = (max_val[0], min_val[1])

#                 if is_point_valid(bottom_left, data) and is_point_valid(top_right, data):
#                     print(f"The point: {min_val, max_val} is valid")
#                     if (max_val[0] - min_val[0] + 1) * (max_val[1]- min_val[1] + 1) > area:
#                         area = (max_val[0] - min_val[0] + 1) * (max_val[1]- min_val[1] + 1)

#     print(area)



# def is_point_valid(coordinates, data):
#     # print(f"Tested point is: {coordinates}")

#     check_top_left, check_bottom_left, check_top_right, check_bottom_right = False, False, False, False
#     # Sorting on first axis
#     sorted_data = sorted(data, key=lambda x: x[0])
#     # data.sort(key=lambda x: x[0])
#     for x_axis, y_axis in sorted_data:
#         if x_axis <= coordinates[0] and y_axis <= coordinates[1]:
#             # print(f"The top left passed: {x_axis, y_axis}")
#             check_top_left = True
        
#         if x_axis <= coordinates[0] and y_axis >= coordinates[1]:
#             # print(f"The bottom left passed: {x_axis, y_axis}")
#             check_bottom_left = True

#     # Sorting on second axis
#     sorted_data = sorted(data, key=lambda x: x[1])
#     for x_axis, y_axis in sorted_data:
#         if y_axis <= coordinates[1] and x_axis >= coordinates[0]:
#             # print(f"The top right passed: {x_axis, y_axis}")
#             check_top_right = True

#         if y_axis >= coordinates[1] and x_axis >= coordinates[0]:
#             # print(f"The bottom right passed: {x_axis, y_axis}")
#             check_bottom_right = True

#     if check_bottom_right == True and check_bottom_left == True and check_top_left == True and check_bottom_left == True:
#         # print("The point is valid")
#         return True
#     return False

# main()