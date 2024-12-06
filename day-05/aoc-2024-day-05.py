from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-05/data/puzzle-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().split('\n\n')

rules = input_lines[0].split()
updates = input_lines[1].split()

result_part_1 = 0
for update in updates:
    pages = update.split(',')
    update_in_correct_order = True
    for idx, current_page in enumerate(pages):

        # Check rules for pages before current page.
        print("pages before current page")
        for other_page_idx in range(0, idx):
            print(current_page, pages[other_page_idx])
            for rule in rules:
                s_r = rule.split('|')
                if current_page == s_r[0] and pages[other_page_idx] == s_r[1]:
                    print("RULE VIOLATION I", s_r[0], '|', s_r[1])
                    update_in_correct_order = False

        # Check rules for pages after current page.
        print("pages after current page")
        for other_page_idx in range(idx + 1, len(pages)):
            print(current_page, pages[other_page_idx])
            for rule in rules:
                s_r = rule.split('|')
                if current_page == s_r[1] and pages[other_page_idx] == s_r[0]:
                    print("RULE VIOLATION II", s_r[0], '|', s_r[1])
                    update_in_correct_order = False

    if update_in_correct_order == True:
        middle_value = pages[(len(pages) - 1) // 2]
        print("middle_value", middle_value)
        result_part_1 += int(middle_value)

print("Answer part 1:", result_part_1)
print("Answer part 2:", 0)
