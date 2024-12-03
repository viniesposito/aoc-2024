import re

def part1(input: str) -> int:
    rows = [x for x in input.splitlines() if x != ""]
    rows = [[int(x) for x in re.findall(r"\d+", row)] for row in rows]

    def is_safe(row: list) -> bool:
        diffs = [row[i] - row[i-1] for i in range(1, len(row))]

        if all(list(map(lambda x: x>0,diffs))) or all(list(map(lambda x: x<0, diffs))):
            if max(map(abs,diffs)) <= 3 and min(map(abs,diffs)) >= 1:
                return True
        
        return False

    return sum(list(map(is_safe, rows)))

test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

print(f"Part 1 test output = {part1(test_input)}")

with open("day2/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

def part2(input: str) -> int:
    rows = [x for x in input.splitlines() if x != ""]
    rows = [[int(x) for x in re.findall(r"\d+", row)] for row in rows]

    def is_safe(row: list) -> bool:
        def sign(num):
            return -1 if num < 0 else 1

        diffs = [row[i] - row[i-1] for i in range(1, len(row))]
        diff_signs = list(map(sign, diffs))
        abs_diffs = list(map(abs, diffs))

        if all(list(map(lambda x: x>0,diffs))) or all(list(map(lambda x: x<0, diffs))):
            if max(abs_diffs) <= 3 and min(abs_diffs) >= 1:
                return True
        return False

    def is_really_safe(row: list, dampen: bool) -> bool:
        def remove_elem_at_index(row: list, i: int) -> list:
            return row[:i] + row[i+1:]

        if is_safe(row) or not dampen:
            return is_safe(row)
        
        for i in range(len(row)):
            if is_safe(remove_elem_at_index(row, i)):
                return True
        
        return False

    return sum([is_really_safe(row, True) for row in rows])

print(f"Part 2 test output = {part1(test_input)}")

with open("day2/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")