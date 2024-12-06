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


# Relative path to the file holding input data.
file_path = path.relpath("day-07/data/test-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().splitlines()

y_size = len(input_lines)
x_size = len(input_lines[0])

visited_locations = [['.'] * x_size for _ in range(y_size)]

start = Point(0, 0)
direction = Direction.NORTH

for y_idx, line in enumerate(input_lines):
    for x_idx, c in enumerate(line):
        if c == '^':
            start.x = x_idx
            start.y = y_idx
            visited_locations[y_idx][x_idx] = 'X'
        if c == "#":
            visited_locations[y_idx][x_idx] = '#'

print("Answer part 1:", 0)
print("Answer part 2:", 0)
