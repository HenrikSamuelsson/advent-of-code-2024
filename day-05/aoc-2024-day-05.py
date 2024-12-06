from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-05/data/test-input.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().split('\n\n')

rules = input_lines[0].split()
updates = input_lines[1].split()



for update in updates:
    pages = update.split(',')
    update_in_correct_order = True
    for idx, current_page in enumerate(pages):
        # Check rules for pages before current page.
        print("pages before current page")
        for other_page_idx in range(0, idx):
            print(current_page, pages[other_page_idx])
        # Check rules far pages after current page.
        print("pages after current page")
        for other_page_idx in range(idx + 1, len(pages)):
            print(current_page, pages[other_page_idx])
        for rule in rules:
            split_rule = rule.split('|')
            #print(split_rule)
            #if page == split_rule[1]:
            #    for page in pages:


print("Answer part 1:", 0)
print("Answer part 2:", 0)
