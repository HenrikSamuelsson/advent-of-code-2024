from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-08/data/test-input-1.txt")

with open(file_path) as input_file:
    input_rows = input_file.read().splitlines()

antenna_map = {}
anti_nodes_map = {}

num_of_rows = len(input_rows)
num_of_cols = len(input_rows[0])

for row_idx, row in enumerate(input_rows):
    for col_idx, value, in enumerate(row):
        if value != '.':
            antenna_map[(row_idx, col_idx)] = value


print("Answer part 1:", 0)
print("Answer part 2:", 0)
