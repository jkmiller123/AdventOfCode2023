# Day 1 of Advent of Code challenge
# Part 1:  read in lines of text and parse out the first and last numeric value
#          the sum those values together to get a final value

import re
import sys

testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day01_sample.txt' if testing else 'Day01_01.txt'
listofwords = ['zerosss', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
listofnumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
d = "one two three four five six seven eight nine".split()

def getTotal(somelines):
        num_lines = re.findall(r'\d+', somelines)
        digit_1 = num_lines[0][0]
        digit_2 = num_lines[-1][-1]

        return digit_1 + digit_2
def convert(n):
    if n in d:
        return str(d.index(n) + 1)

    else :
        return n

def part_1(a_file):
    # new code "borrowed" for simplistic reading of small files.
    with open(a_file) as f:
        lines = f.read().splitlines()

    running_total = 0
    for aline in lines:
        digit_combined = getTotal(aline)
        if testing:
            print("", digit_combined, "", aline)

        running_total = running_total + int(digit_combined)

    print("Grand Total for step 1 = ", getTotal(lines))

def part_2(a_file):
    with open(a_file) as f:
        lines = f.read().splitlines()
    running_total = 0

    for aline in lines:
        newline = aline
        for y in range(len(newline)):
            for x in listofwords:
                newsting = newline[y:y+len(x)]
                if newsting == x:
                    whichword = listofwords.index(x)
                    newline = newline.replace(x, str(listofnumbers[whichword]),1)
        # print(aline, " - " , newline)
        digit_combined = getTotal(newline)
        digits = list(map(convert, re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", aline)))
        if int(digits[0] + digits[-1]) != int(digit_combined):
            print("not mine = ", int(digits[0] + digits[-1]) , " mine = ", digit_combined , aline   )

        # print(digit_combined)
        running_total = running_total + int(digit_combined)


        # print("Grand Total for step 2 = ", running_total)

# part_1(file2read)   # correct answer is 55123
part_2(file2read)  # 54751  is too low...  -- 55255 is not correct
# 55260 should be the correct value

