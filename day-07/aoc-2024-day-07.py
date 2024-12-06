from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-06/data/test-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().splitlines()

print("Answer part 1:", 0)
print("Answer part 2:", 0)
