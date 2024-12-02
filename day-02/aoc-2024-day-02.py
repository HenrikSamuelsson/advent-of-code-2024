from os import path

# Relative path to the file holding input data.
file_path = path.relpath("day-02/data/puzzle-input-aoc-2024-day-02.txt")

with open(file_path) as input_file:
    input_lines = input_file.read().splitlines()

print(input_lines)
line_count = 0

safe_reports_count = 0
for line in input_lines:
    report_chars = line.split()
    report = [int(s) for s in report_chars]
    print(report)
    report_is_safe = True
    if report[0] == report[1]:
        report_is_safe = False
    elif report[0] < report[1]:
        # Could be an increasing report, check entire report.
        for i in range(1,len(report)):
            if report[i-1] > report[i]:
                # Report is not increasing here.
                report_is_safe = False
                break
            if report[i] - report[i-1] > 3:
                # Report increased too much here.
                report_is_safe = False
                break
            if report[i] - report[i-1] < 1:
                # Report did not increase here.
                report_is_safe = False
                break
    else:
        # Could be an decreasing report, check entire report.
        for i in range(1,len(report)):
            if report[i-1] < report[i]:
                # Report is not decreasing here.
                report_is_safe = False
                break
            if report[i-1] - report[i] > 3:
                # Report decreased too much here.
                report_is_safe = False
                break
            if report[i-1] - report[i] < 1:
                # Report here did not decrease here.
                report_is_safe = False
                break
    
    if report_is_safe:
        print("Safe report number:", line_count)
        safe_reports_count += 1
        
    line_count += 1
        
print("Answer part 1:", safe_reports_count)
print("Answer part 2:", 0)
