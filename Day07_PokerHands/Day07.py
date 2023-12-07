

testing = False   # used for debugging messages and to pick the file
stage_1 = True    # used for more complex coding changes
file2read = 'Sample.txt' if testing else 'Data.txt'

# create the default order, realized after typing it in that
# it works better if reversed
# calculate the relative weight for each card and create a dictionary
# to combine with
cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
cards.reverse()
card_strength = {}

for index in range(len(cards)):
    card_strength[cards[index]] = round(index / len(cards), 4)
hand_strength = {'5': 6, '4': 5, "Full": 4, '3': 3, "Two Pair": 2, 'Pair': 1, "High Card": 0 }

# read in the data file
with open(file2read) as f:
    lines = f.read().splitlines()

game = []
for a_line in lines:

    # find out the number of cards that match
    hand = a_line.split(' ')
    num_pair = 0
    num_3ok = 0
    num_matches = 0
    unique_cards = set(hand[0])
    for x in unique_cards:
        num_matches = hand[0].count(x)
        if num_matches > 3:
            break
        elif num_matches == 2:
            num_pair += 1
        elif num_matches == 3:
            num_3ok += 1
    if num_matches > 3:
        this_hand = str(num_matches)
    elif num_3ok == 1 and num_pair == 1:
        this_hand = "Full"
    elif num_3ok == 1:
        this_hand = str(3)
    elif num_pair == 2:
        this_hand = "Two Pair"
    elif num_pair == 1:
        this_hand = "Pair"
    else:
        this_hand = "High Card"
    print("hand= ", hand[0], unique_cards , this_hand, num_matches)
    this_hand_strength = hand_strength[this_hand]
    for x in range(len(hand[0])):
        this_hand_strength = this_hand_strength + (card_strength[hand[0][x]] / (100 ** x ))
    #    print( card_strength[hand[0][x]] / (100 ** x ) , card_strength[hand[0][x]] , x , hand[0][x] )

  #  print(hand[0], " is ", this_hand , ' has rank of ', hand_strength[this_hand], this_hand_strength)
    game.append((this_hand_strength , hand[0],hand[1],this_hand))

game.sort()
total_score = 0
for index in range(len(game)):
    total_score += int(game[index][2]) * ( index +1 )
 #   print("hand = ", game[index][0], game[index][1],int(game[index][2]) * ( index +1 ), " as rank value" )

print("total winnigs are ", total_score)
# part 1: 250232501 is correct