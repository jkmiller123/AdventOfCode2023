import math
import re

testing = False  # used for debugging messages and to pick the file
stage_1 = True  # used for more complex coding changes
file2read = 'Sample.txt' if testing else 'Data.txt'

boxes = [[] for x in range(256)]

# bug encountered with the split function.  if there are no other characters in the line then it adds
# an extra character.  instead of having 10, it adds 11 for the sample file
def parse_data_list(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    return [[x for x in line_in.split('')] for line_in in open(a_file)]

#   blocks = [[y for y in list(blocks)] for blocks in f.read().strip().split("\n")]

with open(file2read) as f:
    groups = f.read().strip().split(",")

def elf_hash(str):
    total = 0
    multiplier = 17
    divisor = 256
    for letters in str:
        total += ord(letters)
        total *= multiplier
        total %= divisor
       # print(letters , " --> ", total )
    return total

new_sum = 0
for items in groups:
    newsplit = re.split("[=-]",items)
    new_sum += elf_hash(items)
    box_to_use = elf_hash(newsplit[0])
    found_it = False
    size_of_box = len(boxes[box_to_use])
    aaa = items.find("=")
    action = '=' if items.find("=") > 0 else '-'
    for counter in range(len(boxes[box_to_use])):
        lens = boxes[box_to_use][counter]
        if lens[0] == newsplit[0]:
            found_it = True
            if action == '-':
                boxes[box_to_use].remove(lens)
                break
            else:
                boxes[box_to_use][counter] = [newsplit[0],newsplit[1]]
                print("found an equal sign")

    if not found_it and action == '=':
        boxes[box_to_use].append([newsplit[0],newsplit[1]])
    print("- ", items, " becomes ", elf_hash(items))
print("Part I :  Total hashed =", new_sum)

total = 0
for counter in range(len(boxes)):
    if boxes[counter] != []:
        for counter2 in range(len(boxes[counter])):
            subtotal = ( counter + 1 ) * (int(boxes[counter][counter2][1]) * (counter2 + 1))
            total += subtotal
            print("Box Number = %3d" % (counter), " contains ", boxes[counter] , " .. ", subtotal)
# part 1:  511416 is correct
print("Part II total = ", total)