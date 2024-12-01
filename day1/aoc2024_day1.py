import re

def part1(input):
    lines = [re.findall(r"\d+",x) for x in input.splitlines() if x != ""]
    list1 = [int(x[0]) for x in lines]
    list1.sort()
    list2 = [int(x[1]) for x in lines]
    list2.sort()
    dists = [abs(x-y) for x,y in zip(list1,list2)]
    return sum(dists)

test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

print(f"Part 1 test output = {part1(test_input)}")

with open("day1/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

def part2(input):
    lines = [re.findall(r"\d+",x) for x in input.splitlines() if x != ""]
    list1 = [int(x[0]) for x in lines]
    list2 = [int(x[1]) for x in lines]
    vals = [list2.count(item)*item for item in list1]
    return sum(vals)

print(f"Part 2 test output = {part1(test_input)}")

with open("day1/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")