from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-01/data/puzzle-input-aoc-2024-day-01.txt")

with open(file_path) as input_file:
    location_ids = input_file.readlines()
print(location_ids)

split_location_ids = [loc_id.split() for loc_id in location_ids]
print(split_location_ids)

left_ids = [int(loc_id[0]) for loc_id in split_location_ids]
print(left_ids)

right_ids = [int(loc_id[1]) for loc_id in split_location_ids]
print(right_ids)

left_ids.sort()
print(left_ids)

right_ids.sort()
print(right_ids)

distances = [abs(left - right) for left, right in zip(left_ids, right_ids)]
print(distances)

total_distance = sum(distances)
print(total_distance)
