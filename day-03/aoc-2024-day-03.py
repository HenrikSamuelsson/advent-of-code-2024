from os import path
import re

# Relative path to the file holding input data.
file_path = path.relpath("day-03/data/puzzle-input-aoc-2024-day-03.txt")

with open(file_path) as input_file:
    input_lines = input_file.read()
    line = input_lines.replace('\n', '')
    print(input_lines)

pattern = r'mul\(\d{1,3},\d{1,3}\)'

answer_part_1 = 0

filtered_words = re.findall(pattern, line)
#print(filtered_words)

for word in filtered_words:
    parts = word.split(',')
    # print(parts)
    number1 = int(re.sub(r'\D', '', parts[0]))
    # print(number1)
    number2 = int(re.sub(r'\D', '', parts[1]))
    # print(number2)
    answer_part_1 += number1 * number2

answer_part_2 = 0


# Start with the header part before the first don't() instruction.
header = line.split("don't()")[0]
print("header", header)

filtered_words = re.findall(pattern, header)
print(filtered_words)

for word in filtered_words:
    parts = word.split(',')
    #print(parts)
    number1 = int(re.sub(r'\D', '', parts[0]))
    #print(number1)
    number2 = int(re.sub(r'\D', '', parts[1]))
    #print(number2)
    answer_part_2 += number1 * number2

result = re.findall("do\(\)(.*?)don't\(\)", line)
print("result", result)

for s in result:
    filtered_words = re.findall(pattern, s)
    print(filtered_words)

    for word in filtered_words:
        parts = word.split(',')
        print(parts)
        number1 = int(re.sub(r'\D', '', parts[0]))
        print(number1)
        number2 = int(re.sub(r'\D', '', parts[1]))
        print(number2)
        answer_part_2 += number1 * number2

print("Answer part 1:", answer_part_1)
print("Answer part 2:", answer_part_2)
