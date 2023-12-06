

testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day04_Sample.txt' if testing else 'Day04_01.txt'

total_wins = 0
total_scratchers = []
with open(file2read) as f:
    lines = f.read().splitlines()

max_cards = len(lines)
num_card_instances = [1]*(max_cards+1)    #Number of instances of each card
num_card_instances[0] = 0  # Python starts counting a 0

for a_line in lines:
    # split_1 [0] Card 1:
    # split_1 [1] 41 .. | 83..
    # split_2 [0] 41 .. 17
    # split_2 [1] 83 .. 53
    split_1 = a_line.split(":")
    split_2 = split_1[1].split("|")
    card_num = int(split_1[0][5:])

    winners = split_2[0].split(" ")
    mynumbers = split_2[1].split(" ")

    # clean up the data by removing the spaces or blanks
    while "" in winners:
        winners.remove("")
    while "" in mynumbers:
        mynumbers.remove("")

    # count the number of matches per card
    for y in range(num_card_instances[card_num]):
        match_number = 0
        for drawnumber in mynumbers:
            if winners.count(drawnumber) > 0:
                match_number += winners.count(drawnumber)

        # print("Card Num:", card_num, " number of matches: ", match_number)
        for x in range(1, match_number + 1):
            next_card = card_num + x
            if next_card < max_cards:
                num_card_instances[next_card] += 1

    # ugly code to calculate the total per card
    # 1 match = 1, 2 matches = 2, 3 matches = 4, 4 matches = 8
    running_total = 0
    for y in range(match_number + 1):
        #  running_total = 1 if y == 1 else running_total * 2
        # or to spell it out
        if y == 1:
            running_total += 1
        else:
            running_total *= 2

    total_wins += running_total
    # print(" Card ", card_num, " has ", match_number, " matches " , running_total, " -- " , total_wins)

print("Total winning value = ", total_wins)
# 979 is too low
# 23750 is the correct answer.
print("Total cards = ", len(total_scratchers))
new_total = 0
for x in num_card_instances:
    new_total += x
print("Total cards", new_total)
# 13260933 Too low  ( and too slow ) 
print(num_card_instances)