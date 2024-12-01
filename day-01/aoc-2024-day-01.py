from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-01/data/puzzle-input-aoc-2024-day-01.txt")

with open(file_path) as input_file:
    location_ids = input_file.readlines()

split_location_ids = [loc_id.split() for loc_id in location_ids]
left_ids = [int(loc_id[0]) for loc_id in split_location_ids]
right_ids = [int(loc_id[1]) for loc_id in split_location_ids]
left_ids.sort()
right_ids.sort()
distances = [abs(left - right) for left, right in zip(left_ids, right_ids)]
total_distance = sum(distances)

similarity_score = []
for right_id in right_ids:
    match_count = 0
    for left_id in left_ids:
        if right_id == left_id:
            match_count += 1
    similarity_score.append(right_id * match_count)
total_similarity_score = sum(similarity_score)

print("Answer part 1:", total_distance)
print("Answer part 2:", total_similarity_score)
