import re

def process_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        input = file.read()
    return input  

def solve_p1(input):
    pattern = re.compile(r"mul\((\d+),\s*(\d+)\)")
    matches = pattern.findall(input)

    sum = 0
    for a, b in matches:
        sum += int(a) * int(b)
    return sum

def solve_p2(input):
    delimiter = ")"
    chunks =  [c+delimiter for c in input.split(delimiter) if c] # could also probably use re library

    mul_pattern = re.compile(r"mul\((\d+),\s*(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don\'t\(\)")

    do = True
    sum = 0
    for chunk in chunks:
        if do:
            mul_match = mul_pattern.search(chunk)
            if mul_match is not None:
                a, b = mul_match.groups()
                sum += int(a) * int(b)
                # print(f"New sum: {sum} from {chunk}")
            elif dont_pattern.search(chunk) is not None:
                # print(f"Disabled: {chunk}")
                do = False
        else:
            if do_pattern.search(chunk) is not None:
                # print(f"Enabled: {chunk}")
                do = True
    return sum

def main():
    input = process_input()
    p1 = solve_p1(input)
    p2 = solve_p2(input)
    print(solve_p2("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))
    return p1, p2

print(main())