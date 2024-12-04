from os import path


def word_at_north(word, c, line_count, col_count, lines_max, cols_max):
    result = False
    # TODO
    return result


# Relative path to the file holding input data.
file_path = path.relpath("day-04/data/test-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().splitlines()

# The word that we are searching for.
word = "XMAS"

# Length of the word that we are searching for
word_length = len(word)

lines_max = len(input_lines)
cols_max = len(input_lines[0])

# Number of times we have found the word that we are searching for.
word_count = 0

line_count = 0
for line in input_lines:
    col_count = 0
    for c in line:
        if word_at_north(word, c, line_count, col_count, lines_max, cols_max):
            word_count += 1
        col_count += 1
    line_count += 1

print("Answer part 1:", word_count)
print("Answer part 2:", 0)
