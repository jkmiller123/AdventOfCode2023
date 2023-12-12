testing = False  # used for debugging messages and to pick the file
stage_1 = False  # used for more complex coding changes
file2read = 'Sample.txt' if testing else 'Data.txt'
distance_factor = 10 if stage_1 else 1000000


# bug encountered with the split function.  if there are no other characters in the line then it adds
# an extra character.  instead of having 10, it adds 11 for the sample file
def parse_data_list(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
   return [[x for x in line_in.split('.')] for line_in in open(a_file).readlines()]

with open(file2read) as f:
    lines2 = f.read().splitlines()
lines3 = parse_data_list(file2read)

lines = [[]]
for row_counter in range(len(lines2)):
    for col_counter in range(len(lines2[row_counter])):
        lines[row_counter].append(lines2[row_counter][col_counter])
    if row_counter < len(lines2) - 1:
        lines.append([])

max_rows = len(lines)
max_cols = len(lines[0])

list_of_rows_to_add = []
for y in range(max_cols):
    found_blank_row = True
    for x in range(max_rows):
        if lines[y][x] == "#":
            found_blank_row = False
            break
    if found_blank_row:
        list_of_rows_to_add.append(y)

list_of_columns_to_add = []
for x in range(max_rows):
    found_blank_col = True
    for y in range(max_cols):
        if lines[y][x] == "#":
            found_blank_col = False
            break
    if found_blank_col:
        list_of_columns_to_add.append(x)

print("Columns to Add :", list_of_columns_to_add)
print("Rows to Add: ", list_of_rows_to_add)
list_of_columns_to_add.sort(reverse=True)
list_of_rows_to_add.sort(reverse=True)
#
# blank_row = ['.' for x in range(max_cols) ]
# for items in list_of_rows_to_add:
#     lines.insert(items, ['.' for x in range(max_cols) ])
#
# for items in list_of_columns_to_add:
#     for y in range(len(lines)):
#         lines[y].insert(items, '.' )

galaxies = []
max_rows = len(lines)
max_cols = len(lines[0])
for y in range(max_rows):
    for x in range(max_cols):
        if lines[y][x] == '#':
            galaxies.append((x,y))
pair_galaxies = []
total_distance = 0
for x in range(len(galaxies)):
    x1,y1 = galaxies.pop()
    for x2,y2 in galaxies:
        add_distance = 0
        for blank_gal in list_of_columns_to_add:
            if x1 < blank_gal < x2 or x1 > blank_gal > x2:
                add_distance += 1

        for blank_gal in list_of_rows_to_add:
            if y1 < blank_gal < y2 or y1 > blank_gal > y2:
                add_distance += 1
        distance = abs(x1 - x2) + abs(y1 - y2) + add_distance * distance_factor - add_distance
        pair_galaxies.append(((x1,y1),(x2, y2), (distance , add_distance * distance_factor - add_distance)))
        total_distance += distance

#for (x1,y1), (x2,y2) , c in pair_galaxies:
#for pairs in pair_galaxies:
#    print(pairs)

print("Total Distance = ", total_distance)
# correct answer 10231178
# stage 2 : 622121609066  too high
#           622120986954  is correct
