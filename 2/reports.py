from collections import Counter

def process_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read()
    lines = lines.split("\n")

    reports = []
    for report in lines:
        report = report.split(" ")
        for i, level in enumerate(report):
            report[i] = int(level)
        reports.append(report)
    return reports

def check_safe(pairs, ascending):
    if ascending:
        return int(all(x < y and 0 < (y - x) <= 3 for x, y in pairs))
    else:
        return int(all(y < x and 0 < (x - y) <= 3 for x, y in pairs))

def check_safe_p2(pairs, ascending):
    if ascending:
        return int(sum(y <= x or (y - x) == 0 or (y - x) > 3 for x, y in pairs) <= 1)
    else:
        return int(sum(x <= y or (x - y) == 0 or (x - y) > 3 for x, y in pairs) <= 1)

def solve_p1(reports):
    safe = 0
    for report in reports:
        if len(report) <= 1:
            safe += 1
            continue
        ascending = report[0] < report[1]
        pairs = zip(report, report[1:])
        safe += check_safe(pairs, ascending)
    return safe

def solve_p2(reports):
    safe = 0
    for report in reports:
        if len(report) <= 1:
            safe += 1
            continue
        ascending = report[0] < report[1]
        pairs = zip(report, report[1:])
        safe += check_safe_p2(pairs, ascending)
    return safe

def main():
    reports = process_input()
    p1 = solve_p1(reports)
    p2 = solve_p2(reports)
    return p1, p2

print(main())