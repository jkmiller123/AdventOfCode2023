# Day 02 .. grabbing some dice out of a bag
#  hardest part of this task is to parse out the data from the line.
#  each line has a draw number and then one or more sets of dice pulled from the bag
#  each set can contain 0 or more of each colour.  Red, Green or Blue

# Sample data
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# parse by ':' to separate out the draw number from the sets
# parse each set by the ';'
# parse out each die by a space ' '

# Part 1 :  determine if the number of dice pulled is feasibly possible.
# There is a maximum number of colour in the bag.  There are only 13 Greens for example
# if the line has 15 green die being pulled then the elf is playing a trick on you.

# also, as a secondary caution, make sure that the maximum number of dice aren't pulled.
# doubt this will occur, but its better to be safe then error prone.
# add up all the game id's for only the valid games

# Part 2:  leverages most of the same code but now is has every line as valid is looking for
# what the least number of dice could be in each set.   ( in this case least means maximum ;-)
# once the largest number of each dice is found multiple them together to get a product
# and add all the products together to get  total


testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Day02_Samplet.txt' if testing else 'Day02_01.txt'

# specific items for this program
listofcolours = ['green', 'red', 'blue']
max_items = {'green': 13, 'red': 12, 'blue': 14}
max_num_dice =        13 +       12 +        14


def part1(a_file):
    with open(a_file) as f:
        lines = f.read().splitlines()

    sum_of_games = 0
    thisgrab = {}
    for colours in listofcolours:   # create a dictionary of values and set to 0
        thisgrab[colours] = 0

    print(thisgrab)
    for line in lines:
        game_possible = True
        t_split = line.split(":")           # parse out the game id
        game_id = t_split[0].strip("Game")
        sets = t_split[1].split(";")        # parse out the sets
        for x in sets:
            grab = x.split(",")             # parse out each die
            total_dice_grab = 0             # reset counter
            for y in grab:
                z = y.split(" ")            # break out the number of that die pulled
                thisgrab[z[2]] = z[1]
                total_dice_grab = total_dice_grab + int(z[1])
                if int(z[1]) > max_items[z[2]]:   # number of dice per colour exceeds the set maximium
                    game_possible = False
            if total_dice_grab > max_num_dice:
                game_possible = False

            for item in thisgrab:
                print("Game #", game_id , "colour: ", item, " number = ", thisgrab[item])
            print("--")
        if game_possible:
            sum_of_games = sum_of_games + int(game_id)

    print("Sum of all the games = ",sum_of_games)

def  part2(a_file):
    # find the largest number of dice in each set therefore that is the fewest number of dice needed
    with open(a_file) as f:
        lines = f.read().splitlines()

    sum_of_powers = 0
    thisgrab = {}

    print(thisgrab)
    for line in lines:
        t_split = line.split(":")
        game_id = t_split[0].strip("Game")
        sets = t_split[1].split(";")
        for colours in listofcolours:
            thisgrab[colours] = 0

        for x in sets:
            grab = x.split(",")
            for y in grab:
                z = y.split(" ")
                thisgrab[z[2]] = max(thisgrab[z[2]], int(z[1]))

        print("Game #", game_id , end=" ")
        for item in thisgrab:
            print(item, " = ", thisgrab[item], end=" ")

        print("")
        power_set = 1
        for colours in listofcolours:
            power_set *= thisgrab[colours]
        sum_of_powers += power_set

    print("Sum of all the powersets = ", sum_of_powers)

# part1(file2read)   #2541 is the correct answer
part2(file2read)