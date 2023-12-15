import math

testing = False  # used for debugging messages and to pick the file
stage_1 = True  # used for more complex coding changes
file2read = 'Sample.txt' if testing else 'Data.txt'
max_rotates = 3 if testing else 1000000000


# bug encountered with the split function.  if there are no other characters in the line then it adds
# an extra character.  instead of having 10, it adds 11 for the sample file
def parse_data_list(a_file):
    # this will create a list of lists.  not exactly what I was looking for.
    # prefer to make an array with definite co-ordinates.
    return [[x for x in line_in.split('')] for line_in in open(a_file)]


with open(file2read) as f:
    blocks = [[y for y in list(blocks)] for blocks in f.read().strip().split("\n")]

num_cols = len(blocks[0])
num_rows = len(blocks)
x: int = 0
def roll_north():
    for x in range(num_cols):
        last_blank = 0
        for y in range(num_rows):
            this_value = blocks[y][x]
            if blocks[y][x] == '#':
                last_blank = y + 1
            elif blocks[y][x] == 'O':
                if last_blank != y:
                    blocks[last_blank][x] = 'O'
                    blocks[y][x] = '.'
                    last_blank += 1
                else:
                    last_blank = y + 1
def roll_south():
    for x in range(num_cols):
        last_blank = num_rows -1
        for y in range(num_rows - 1, -1, -1):
            this_value = blocks[y][x]
            if blocks[y][x] == '#':
                last_blank = y - 1
            elif blocks[y][x] == 'O':
                if last_blank != y:
                    blocks[last_blank][x] = 'O'
                    blocks[y][x] = '.'
                    last_blank -= 1
                else:
                    last_blank = y - 1
def roll_west():
    somedata = blocks
    for y in range(num_rows):
        last_blank = num_cols - 1
        for x in range(num_cols - 1, -1 , -1):
            this_value = blocks[y][x]
            if blocks[y][x] == '#':
                last_blank = x - 1
            elif blocks[y][x] == 'O':
                if last_blank != x:
                    blocks[y][last_blank] = 'O'
                    blocks[y][x] = '.'
                    last_blank -= 1
                else:
                    last_blank = x - 1
def roll_east():
    somedata = blocks
    for y in range(num_rows):
        last_blank = 0
        for x in range(0, num_cols, 1):
            this_value = blocks[y][x]
            if blocks[y][x] == '#':
                last_blank = x + 1
            elif blocks[y][x] == 'O':
                if last_blank != x:
                    blocks[y][last_blank] = 'O'
                    blocks[y][x] = '.'
                    last_blank = last_blank + 1
                else:
                    last_blank = x + 1
import time

# get the start time
st = time.time()
avalue = hash(str(blocks))
prev_blocks = { avalue }
for counter in range(max_rotates):
    if counter % 10000 == 0 and counter > 0:
        # get the end time
        et = time.time()
        # get the execution time
        elapsed_time = et - st
        print(counter, 'Execution time:', elapsed_time, 'seconds')
    roll_north()
    roll_east()
    roll_south()
    roll_west()
    total = 0
    for y in range(num_rows-1):
        for x in range(num_cols):
            if blocks[y][x] == 'O':
                total += 1 * (num_rows - y )
    if 105602 < total < 105608:
        print(" Hmmm.  ", total, " At ", counter)

    avalue = hash(str(blocks))
    if avalue in prev_blocks:
       print("Found a previous block ", counter)
       break
    else:
       prev_blocks.add(avalue)
new_counter = max_rotates % counter
print("new counter", new_counter)
for counter in range(new_counter - 1 ):
    roll_north()
    roll_east()
    roll_south()
    roll_west()

    total = 0
    for y in range(num_rows-1):
        for x in range(num_cols):
            if blocks[y][x] == 'O':
                total += 1 * (num_rows - y )
    if 105602 < total < 105608:
        print(" Hmmm.  ", total, " At ", counter)
print("The total amount = ",total)

# part II : 105608 is too high
#         : 105602 is too low  // 3
#          :105607 not right
#           105605
#          105604
#  105606... is the right answer... how.. who cares... 