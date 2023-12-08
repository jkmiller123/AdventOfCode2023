
map_start: int = 0
map_end: int = 1
map_offset: int = 2

source_mapping: int = 0
source_start: int = 1
source_range: int = 2

mapping_list = [(0, 999, 0)]

seeds2soil = [(20,50,20),(30,40,20)]
#seeds2soil = [(50, 98,  2) , (52, 50, 48), ( 0, 15, 37) ]#  , (37, 52,  2) , (39, 0, 15)]
soil2fert =  [( 0, 15, 37), (37, 52,  2), (39, 0, 15)]

for entry in seeds2soil:
    map_size = len(mapping_list)
    for index in range(map_size):
         map = mapping_list[index]
         s1 = map[map_start]   # always map[map_start]
         e1 = entry[source_start] -1   # always entry[entry_start] - 1
         d1 = map[map_offset]
         s2 = entry[source_start]   # entry[entry_start ]

         if map[map_start] <= entry[map_end] <= map[map_end]:  # between points
             if map[map_end] < entry[source_start] + entry[source_range]:
                 e2 = map[map_end]
                 d2 = map[map_offset]
                 s3 = map[map_end] + 1
                 e3 = entry[source_start] + entry[source_range]
                 d3 = map[map_offset] + entry[source_mapping] - entry[source_start]
             else:
                 e2 = entry[source_start] + entry[source_range]
                 d2 = map[map_offset] + entry[source_mapping] - entry[source_start]
                 s3 = entry[source_start] + entry[source_range] + 1
                 e3 = map[map_end]
                 d3 = map[map_offset]

             mapping_list[index] = (s1,e1,d1)   # break the first point
             mapping_list.append((s2,e2,d2))
             mapping_list.append((s3,e3,d3))
    mapping_list.sort()
    print("Mapping List > ", mapping_list)


for maps in mapping_list:
    print(maps)