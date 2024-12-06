import re

def part1(input: str) -> int:
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

    output = 0
    for instruction in instructions:
        x, y = re.findall(r"\d{1,3}", instruction)
        output += int(x)*int(y)

    return output

test_input = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""

print(f"Part 1 test output = {part1(test_input)}")

with open("day3/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

def part2(input: str) -> int:
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

    instruction_indices = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", input)
    dos_indices = re.finditer(r"do\(\)", input)
    donts_indices = re.finditer(r"don't\(\)", input)

    instruction_indices = [i.start() for i in instruction_indices]
    dos_indices = [i.start() for i in dos_indices]
    donts_indices = [i.start() for i in donts_indices]

    do = True

    def get_largest_smallest_than_n(lst, n):
        tmp = [x for x in lst if x<n]

        return tmp[-1] if tmp else -1

    for i, x in enumerate(instruction_indices):
        last_do = get_largest_smallest_than_n(dos_indices, x)
        last_dont = get_largest_smallest_than_n(donts_indices, x)
        # print(x, last_do, last_dont)
        if last_dont < x and last_dont > last_do:
            instructions[i] = ""

    output = 0
    for instruction in instructions:
        if instruction == "":
            continue
        x, y = re.findall(r"\d{1,3}", instruction)
        output += int(x)*int(y)

    return output

print(f"Part 2 test output = {part2(test_input)}")

with open("day3/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")