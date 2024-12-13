from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-08/data/test-input-1.txt")
with open(file_path) as input_file:
    input_rows = input_file.read().splitlines()

antenna_map = {}
anti_nodes_map = {}
anti_nodes_map_part_2 = {}

num_of_rows = len(input_rows)
num_of_cols = len(input_rows[0])

for row_idx, row in enumerate(input_rows):
    for col_idx, value, in enumerate(row):
        if value != '.':
            antenna_map[(row_idx, col_idx)] = value

for ant_1 in antenna_map:
    print("ant_1", ant_1[0], ant_1[1], antenna_map[ant_1])
    for ant_2 in antenna_map:
        if (ant_1 != ant_2):
            if (antenna_map[ant_1] == antenna_map[ant_2]):
                print("ant_2", ant_2[0], ant_2[1], antenna_map[ant_2])
                delta_y = ant_2[0] - ant_1[0]
                anti_node_y = ant_2[0] + delta_y
                delta_x = ant_2[1] - ant_1[1]
                anti_node_x = ant_2[1] + delta_x
                anti_node_is_on_map = True
                if anti_node_x < 0:
                    anti_node_is_on_map = False
                if anti_node_y < 0:
                    anti_node_is_on_map = False
                if anti_node_x >= num_of_cols:
                    anti_node_is_on_map = False
                if anti_node_y >= num_of_rows:
                    anti_node_is_on_map = False
                if anti_node_is_on_map:
                    anti_nodes_map[(anti_node_y, anti_node_x)] = '#'

antenna_anti_nodes = 0
for ant_1 in antenna_map:
    print("ant_1", ant_1[0], ant_1[1], antenna_map[ant_1])
    for ant_2 in antenna_map:
        step = 0
        if (ant_1 != ant_2):
            if (antenna_map[ant_1] == antenna_map[ant_2]):
                antenna_anti_nodes += 1
                anti_node_is_on_map = True
                print("ant_2", ant_2[0], ant_2[1], antenna_map[ant_2])
                while anti_node_is_on_map == True:
                    step += 1
                    delta_y = ant_2[0] - ant_1[0]
                    anti_node_y = ant_2[0] + delta_y * step
                    delta_x = ant_2[1] - ant_1[1]
                    anti_node_x = ant_2[1] + delta_x * step
                    if anti_node_x < 0:
                        anti_node_is_on_map = False
                    if anti_node_y < 0:
                        anti_node_is_on_map = False
                    if anti_node_x >= num_of_cols:
                        anti_node_is_on_map = False
                    if anti_node_y >= num_of_rows:
                        anti_node_is_on_map = False
                    if anti_node_is_on_map:
                        anti_nodes_map_part_2[(anti_node_y, anti_node_x)] = '#'

print("Answer part 1:", len(anti_nodes_map))
print("Answer part 2:", len(anti_nodes_map_part_2) + )
