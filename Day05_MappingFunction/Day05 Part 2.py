
import time
import sys

testing = True   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day05_Sample.txt' if testing else 'Day05_01.txt'

mapping_order = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']


# read in the data file
with open(file2read) as f:
    lines = f.read().splitlines()

# count how many maps are in the file
num_maps = 0
for a_line in lines:
    if a_line.find("map:") > 0:
        num_maps += 1
# create a list that will hold all the mapping functions
rows, cols = (num_maps, 1)
mapping_values = [["a" for i in range(cols)] for j in range(rows)]

# mapping_values = [["0"]]*(num_maps )
map_counter: int = -2   # there are two blank lines that need to be accounted for
for a_line in lines:
    if a_line != "":   #not a blank line
        if a_line.find(":") > 0:   # even handle the seed line
            map_counter += 1
            row_counter = 0
            header = (a_line.replace(" map:", "")).split("-to-")
        else:
            if row_counter > 0:
                mapping_values[map_counter].append("")
            mapping_values[map_counter][row_counter] = ([int(x) for x in a_line.split(" ")] + header)
            row_counter += 1

# get the seeds to start with
t_seeds = [int(x) for x in lines[0][7:].split(" ")]
num_seed_pairs = int(len(t_seeds)/2)
seeds = [(1,2) for x in range(num_seed_pairs)]
counter = 0
for a in range(num_seed_pairs):
    seeds[a] = (t_seeds[counter], t_seeds[counter+1])
    counter += 2

def map_it(search_value, step_number):
    found_it = False
    # for x in mapping_steps[step_number]:  # change to handle new code
    for x in mapping_values[step_number]:
        if x[1] <= search_value < x[1] + x[2]:
            found_it = True
            b = x[0] + search_value - x[1]
    return b if found_it else search_value

lowest_location = map_it(seeds[0][0],0)
lower_location = lowest_location
for a_seed in seeds:
    print("Seed pair", a_seed[0], " through ", a_seed[1])
    starting_point = a_seed[0]
    ending_range = a_seed[1]
    halfPoint = int(ending_range / 2)

    looking = True
    while looking:
        for map_num in range(len(mapping_values)):
            starting_location = map_it(starting_point, map_num)

        if starting_location < lowest_location:
            lowest_location = starting_location
        if starting_location < lower_location:
            ending_range = halfPoint - starting_point
            halfPoint = starting_point + int(ending_range /2)
            lower_location = starting_location
        else:
            if starting_location == lower_location:
                looking = False
            else:
                starting_point = starting_point + halfPoint
                halfPoint = halfPoint / 2
 #       print(".")

print("The lowest location is: ", lowest_location)
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
