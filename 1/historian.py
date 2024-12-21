from collections import Counter

def process_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read()
    lines = lines.split("\n")

    left_list = []
    right_list = []
    for line in lines:
        left, right = line.split(" ", 1)
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list

def solve_p1(left_list, right_list):
    left_list = sorted(left_list)
    right_list = sorted(right_list)

    sum = 0
    for i, left in enumerate(left_list):
        sum += abs(left - right_list[i])
    return sum

def solve_p2(left_list, right_list):
    sum = 0
    right_freq = Counter(right_list)
    for _, left in enumerate(left_list):
        sum += left * right_freq[left]
    return sum

def main():
    left_list, right_list = process_input()
    p1 = solve_p1(left_list, right_list)
    p2 = solve_p2(left_list, right_list)
    return p1, p2

print(main())