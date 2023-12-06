
# Day 6:  the race time and distances form a parobolic arc, in that the middle time will always produce
# the furest distance.   Therefore start there and keep checking until the new distance is less than
# the distance to beat.

# Repeat the calculation for both sides of the arc ( +/- 1 ) for the checking time

#Time:      7  15   30
#Distance:  9  40  200

testing = False   # used for debugging messages and to pick the file
stage_1 = False    # used for more complex coding changes

sample_race_time = [(7,9), (15,40), (30,200)]
data1_race_time  = [(62,553),(64,1010),(91,1473),(90,1074)]
stage_2_time = [(62649190,553101014731074)]
data_to_use = sample_race_time if testing else data1_race_time if stage_1 else stage_2_time
total_methods = 1
race_num = 1
for race in data_to_use:
    time = race[0]
    d2b = race[1]    # distance to beat  d2b
    check_time = int(race[0] / 2)
    run_time = (time - check_time)
    distance = run_time * check_time
    num_methods = 0
    while distance > d2b:
        num_methods += 1
        # print("Distance = ", distance, " Hold time =", check_time, " run time = ", run_time )
        check_time += 1
        run_time = ( time - check_time)
        distance = run_time * check_time

    # do it again but for the negative side
    check_time = int(race[0] / 2)
    check_time -= 1
    run_time = (time - check_time)
    distance = run_time * check_time

    while distance > d2b:
        num_methods += 1
        # print("Distance = ", distance, " Hold time =", check_time, " run time = ", run_time )
        check_time -= 1
        run_time = ( time - check_time)
        distance = run_time * check_time
    print("Race: ", race_num, " Time = ", race[0], " number of methods = ", num_methods )
    total_methods *= num_methods
    race_num += 1

print("Total Number of Methods = ", total_methods)

# part 1 : 840336 is the correct answer
# part 2 : 41382569 is the correct answer