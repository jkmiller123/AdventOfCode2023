


testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day03_Sample.txt' if testing else 'Day03_01.txt'

with open(file2read) as f:
    lines = f.read().splitlines()

max_x = len(lines)
max_y = len(lines[0])
machine_parts = []
machine_numbers = []
gears = []
# loop though the grid and grab all the machine parts.
# I suspect part 2 will have us look outside of the grid ( other side will count )
for x in range(max_x):
    for y in range(max_y):
        if not (lines[x][y].isdigit() or lines[x][y] == '.'):
            machine_parts.append((x, y , lines[x][y]))
           # print("Found a symbol at ", x , " ", y)
print("there are ", len(machine_parts), " machine parts")

for my_parts in machine_parts:
    x: int
    y: int
    somepart: str
    x, y, somepart = my_parts
#    print("Part ",x, ",",y, " ->", somepart)
    for x1 in range(x-1, x+2):
        for y1 in range(y-1, y + 2):
            if 0 <= x1 <= max_x and 0 <= y1 <= max_y:
                if lines[x1][y1].isdigit():
                    # there is digit, now go find where the number starts and ends.
                    # might be a more elegant way in python, but looping through checking
                    # to see if each item is a digit and stopping when its not.
                    # make sure not to look beyond the boundaries.
                    y2 = y1
                    while y2 >= 0:
                        if lines[x1][y2].isdigit():
                            y2 -= 1
                        else:
                            break

                    y3 = y1
                    while y3 < max_y:
                        if lines[x1][y3].isdigit():
                            y3 += 1
                        else:
                            break
                    thenum = lines[x1][y2+1:y3]
                    machine_numbers.append(((x,y),thenum,somepart))  # create list of all the info

running_total = 0
running_gear_total = 0
final_numbers = set(machine_numbers)  # remove duplicates
for parts in final_numbers:
    running_total += int(parts[1])
    if parts[2] == '*':             # isolate only the gears
        gears.append(parts)

gears.sort()   # sort the gears by the address to make the compare
for counter in range(len(gears) -1):
    if gears[counter][0] == gears[counter + 1][0]:    # since there are only 2 gears, just look forward
        running_gear_total += int(gears[counter][1]) * int(gears[counter+1][1])


print("Part 1:  Total sum of parts = %9d" % running_total)
print("Part 2:  Total gear ratio   = %9d" % running_gear_total)