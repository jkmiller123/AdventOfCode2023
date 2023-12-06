
map_start = 0
map_end = 1
map_offset = 2

source_start = 1
source_range = 2

mapping_list = [(0, 999, 0)]

seeds2soil = [(50, 98,  2) ] # , (52, 50, 48)]
soil2fert =  [( 0, 15, 37), (37, 52,  2), (39, 0, 15)]

for entry in seeds2soil:
    for index in range(len(mapping_list)):
        map = mapping_list[index]
        if map[map_start] <= entry[map_end] <= map[map_end]:   # between points
            prev_peak = map[map_end]
            mapping_list[index] = [(map[map_start], entry[source_start] - 1, map[map_offset])]   # break the first point
            if map[map_end] > entry[source_start] + entry[source_range]:   # is this one continous range
                mapping_list.append([(entry[1], entry[1]+entry[2] - 1, map[0] + entry[1] - entry[0])])
                mapping_list.append([(entry[1]+entry[2], prev_peak, map[0])])
            else:
                mapping_list.append([(map[map_end], entry[source_start] + entry[source_range]), ])


for maps in mapping_list:
    print(maps)