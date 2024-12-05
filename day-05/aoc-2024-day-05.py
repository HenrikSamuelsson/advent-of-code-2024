from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-05/data/test-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().split('\n\n')

print(input_lines)

rules = input_lines[0].split()
updates = input_lines[1].split()

print(rules)
print(updates)

print("Answer part 1:", 0)
print("Answer part 2:", 0)
