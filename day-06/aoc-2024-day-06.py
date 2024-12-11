from dataclasses import dataclass
from enum import Enum
from os import path


@dataclass
class Point:
    x: int
    y: int


class Direction(Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


def next_direction(current_direction):
    if current_direction == Direction.NORTH:
        return Direction.EAST
    if current_direction == Direction.EAST:
        return Direction.SOUTH
    if current_direction == Direction.SOUTH:
        return Direction.WEST
    if current_direction == Direction.WEST:
        return Direction.NORTH


obstacle = '#'  # Marks an obstacle.
visited = 'X'  # Marks a position known to be visited by the guard.
safe = '.'  # Marks a position not yet seen to be visited by the guard.
guard = '^'  # Current position of the guard.
new_obstacle = 'O'  # A new obstacle placed by us in the lab.

# Relative path to the file holding input data.
file_path = path.relpath("day-06/data/puzzle-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().splitlines()

y_size = len(input_lines)
x_size = len(input_lines[0])

position = Point(0, 0)
direction = Direction.NORTH

# Build initial map of the lab
lab_map = [[safe] * x_size for _ in range(y_size)]
for y_idx, line in enumerate(input_lines):
    for x_idx, marker in enumerate(line):
        if marker == guard:
            position.x = x_idx
            position.y = y_idx
            lab_map[y_idx][x_idx] = guard
        if marker == "#":
            lab_map[y_idx][x_idx] = obstacle

# Let the guard traverse the map
while True:
    # Mark current guard position as visited
    lab_map[position.y][position.x] = visited

    # Check what guard will do next, based on direction and position
    if direction == Direction.NORTH:
        if position.y - 1 < 0:
            break   # We are done because guard will leave the lab map.
        if lab_map[position.y - 1][position.x] == obstacle:
            direction = next_direction(direction)
            continue
        position.y -= 1

    if direction == Direction.EAST:
        if position.x + 1 >= x_size:
            break   # We are done because guard will leave the lab map.
        if lab_map[position.y][position.x + 1] == obstacle:
            direction = next_direction(direction)
            continue
        position.x += 1

    if direction == Direction.SOUTH:
        if position.y + 1 >= y_size:
            break   # We are done because guard will leave the lab map.
        if lab_map[position.y + 1][position.x] == obstacle:
            direction = next_direction(direction)
            continue
        position.y += 1

    if direction == Direction.WEST:
        if position.x - 1 < 0:
            break   # We are done because guard will leave the lab map.
        if lab_map[position.y][position.x - 1] == obstacle:
            direction = next_direction(direction)
            continue
        position.x -= 1

print("Guards leaves map from", position.x, position.y)

visited_positions = 0
for line in lab_map:
    for c in line:
        if c == visited:
            visited_positions += 1

print("Answer part 1:", visited_positions)

position = Point(0, 0)
direction = Direction.NORTH

# Part 2.
lab_map = [[safe] * x_size for _ in range(y_size)]
for y_idx, line in enumerate(input_lines):
    for x_idx, marker in enumerate(line):
        if marker == guard:
            position.x = x_idx
            position.y = y_idx
            lab_map[y_idx][x_idx] = guard
        if marker == "#":
            lab_map[y_idx][x_idx] = obstacle

original_marker = safe
times_guard_stuck = 0

for y_idx, line in enumerate(lab_map):
    for x_idx, marker in enumerate(line):
        if marker == safe or marker == visited:
            original_marker = safe
            # Place a new obstacle on the lab map.
            lab_map[y_idx][x_idx] = new_obstacle

            # Let the guard traverse the map
            guard_got_out = False
            step_count = 0
            step_max = len(lab_map) * (len(line))
            while step_count <= step_max:
                # Mark current guard position as visited
                lab_map[position.y][position.x] = visited

                # Update guard movement, based on direction and position.
                if direction == Direction.NORTH:
                    if position.y - 1 < 0:
                        guard_got_out = True
                        break   # We are done, guard will leave the lab map.
                    if lab_map[position.y - 1][position.x] == obstacle or lab_map[position.y - 1][position.x] == new_obstacle:
                        direction = next_direction(direction)
                        continue
                    position.y -= 1
                    step_count += 1

                if direction == Direction.EAST:
                    if position.x + 1 >= x_size:
                        guard_got_out = True
                        break   # We are done, guard will leave the lab map.
                    if lab_map[position.y][position.x + 1] == obstacle or lab_map[position.y][position.x + 1] == new_obstacle:
                        direction = next_direction(direction)
                        continue
                    position.x += 1
                    step_count += 1

                if direction == Direction.SOUTH:
                    if position.y + 1 >= y_size:
                        guard_got_out = True
                        break   # We are done, guard will leave the lab map.
                    if lab_map[position.y + 1][position.x] == obstacle or lab_map[position.y + 1][position.x] == new_obstacle:
                        direction = next_direction(direction)
                        continue
                    position.y += 1
                    step_count += 1

                if direction == Direction.WEST:
                    if position.x - 1 < 0:
                        guard_got_out = True
                        break   # We are done, guard will leave the lab map.
                    if lab_map[position.y][position.x - 1] == obstacle or lab_map[position.y][position.x - 1] == new_obstacle:
                        direction = next_direction(direction)
                        continue
                    position.x -= 1
                    step_count += 1

            if guard_got_out:
                print("Guards leaves map from", position.x, position.y)
            else:
                print("Guard got stuck")
                times_guard_stuck += 1

            # Clean up by setup the original map for next round
            position = Point(0, 0)
            direction = Direction.NORTH
            lab_map = [[safe] * x_size for _ in range(y_size)]
            for y, line in enumerate(input_lines):
                for x, marker in enumerate(line):
                    if marker == guard:
                        position.x = x
                        position.y = y
                        lab_map[y][x] = guard
                    if marker == obstacle:
                        lab_map[y][x] = obstacle

print("Answer part 2:", times_guard_stuck)
