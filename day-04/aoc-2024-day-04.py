from os import path


def word_at_north(word, input_lines, line_count, col_count):
    # Start by checking if word will fit.
    if word_length > line_count + 1:  # Add 1 because line count starts at 0.
        # Word is too long to fit horizontally
        return False
    # Check if all characters in the word are present.
    for idx, c in enumerate(word):
        line = input_lines[line_count - idx]
        if word[idx] != line[col_count]:
            return False
    print("Word at north from line", line_count, "column", col_count)
    return True


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
    for position in line:
        if word_at_north(word, input_lines, line_count, col_count):
            word_count += 1
        col_count += 1
    line_count += 1

print("Answer part 1:", word_count)
print("Answer part 2:", 0)
