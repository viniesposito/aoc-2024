# imports
import re

# part 1 code
def part1(input: str) -> int:
    rules = re.findall(r"\d{2}\|\d{2}", input)
    rules = [(int(x[:2]), int(x[3:])) for x in rules]

    updates = [re.findall(r"^\d{2}(?:,\d{2})*\n*$", line) for line in input.strip().split("\n")]
    updates = [x[0].split(",") for x in updates if x]
    updates = [[int(y) for y in x] for x in updates]

    def get_sorted_update(update: list) -> bool:
        def compare_nums(x, y):
            if [rule for rule in rules if rule == (x,y)]:
                return True
            if [rule for rule in rules if rule == (y,x)]:
                return False
            return ValueError("Pair is not in rules")

        x = update[0]

        sorted_update = []

        for i in range(1, len(update)):
            y = update[i]
            if i == 1:
                if compare_nums(x,y):
                    sorted_update.append(x)
                    sorted_update.append(y)
                else:
                    sorted_update.append(y)
                    sorted_update.append(x)
            else:
                for j in range(len(sorted_update)):
                    if compare_nums(y, sorted_update[j]):
                        sorted_update.insert(j-1, y)
                        break
                sorted_update.append(y)

        return sorted_update

    count = 0

    for update in updates:
        if update == get_sorted_update(update):
            count += update[int(len(update)/2)]

    return count

test_input = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

# part 1 outputting
print(f"Part 1 test output = {part1(test_input)}")

with open("day5/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

# part 2 code
def part2(input: str) -> int:
    rules = re.findall(r"\d{2}\|\d{2}", input)
    rules = [(int(x[:2]), int(x[3:])) for x in rules]

    updates = [re.findall(r"^\d{2}(?:,\d{2})*\n*$", line) for line in input.strip().split("\n")]
    updates = [x[0].split(",") for x in updates if x]
    updates = [[int(y) for y in x] for x in updates]

    def get_sorted_update(update: list) -> bool:
        def compare_nums(x, y):
            if [rule for rule in rules if rule == (x,y)]:
                return True
            if [rule for rule in rules if rule == (y,x)]:
                return False
            return ValueError("Pair is not in rules")

        x = update[0]

        sorted_update = []

        for i in range(1, len(update)):
            y = update[i]
            if i == 1:
                if compare_nums(x,y):
                    sorted_update.append(x)
                    sorted_update.append(y)
                else:
                    sorted_update.append(y)
                    sorted_update.append(x)
            else:
                for j in range(len(sorted_update)):
                    # compare_nums(47, 97) = False
                    # compare_nums(47, 75) = False
                    if compare_nums(y, sorted_update[j]):
                        sorted_update.insert(j, y)
                        break
                    elif j == len(sorted_update) - 1:
                        sorted_update.append(y)

        return sorted_update

    count = 0

    for update in updates:
        sorted_update = get_sorted_update(update)
        if update != sorted_update:
            # print(update, sorted_update)
            count += sorted_update[int(len(sorted_update)/2)]

    return count

# part 2 outputting
print(f"Part 2 test output = {part2(test_input)}")

with open("day5/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")