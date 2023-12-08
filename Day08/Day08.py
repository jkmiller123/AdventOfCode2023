# Needed some help today.  not going to lie. the Concept of the LCM throws me for a loop


import re
from math import lcm

testing = False   # used for debugging messages and to pick the file
stage_1 = False    # used for more complex coding changes
file2read = 'Sample.txt' if testing else 'Data.txt'

stopping_point = 'ZZZ'
# read in the data file
with open(file2read) as f:
    lines = f.read().splitlines()

instructions = lines[0]
num_instructions = len(instructions)
docs = {}
for a_line in lines:
    if a_line != instructions and a_line != '':
        split_line = a_line.split(" = ")
        docs[split_line[0]] = re.sub("[( )]","",split_line[1]).split(",")

def pr_debug(step_counter, step, next_instruction):
    print("Step %3d" % step_counter, " Current:", step , " docs ", end="" )
    if next_instruction == "L":
        print("\033[92m\033[1m%s\033[0m" % docs[step][0] , " ," , docs[step][1], end= "")
    else:
        print(docs[step][0], " , \033[92m\033[1m%s\033[0m" % docs[step][1], end= "")

    print(" instruction:", next_instruction )
    return
# step = "AAA"
def find_path(step):
    step_counter = 0
    while ( stage_1 and step != 'ZZZ') or ( not stage_1 and step[-1] != 'Z'):
        a = step_counter % num_instructions
        next_instruction = instructions[a]
        next_step = docs[step][0] if next_instruction == "L" else docs[step][1]
       # pr_debug(step_counter, step, next_instruction)
        step_counter += 1
        step = next_step

    return step_counter

# Part 1:
moves = {('AAA',0)}
distances = []
for x in moves:
    distances.append(find_path(x[0]))

print("The number for part 1 :", lcm(*distances))

moves = {}
for item in docs:
    if item[-1] == 'A':
        moves[item] = 0
distances2 = []
for x in moves:
    distances2.append(find_path(x))

print("The number for part 2 :", lcm(*distances2))
# Part 1:  921 too low
# 18727 is the correct answer for part 1

# PART 2
# 18024643846273
# 18024643846273
# Think of it as 6 different sine waves that will eventually converge on the same spot.  what is that spot
# Least Common Multiplier  ( LCM ) can be used to generate that point
# they are sine waves because they all repeat after a reaching the one and only __Z for each starting point
# but how do you figure that out ??
