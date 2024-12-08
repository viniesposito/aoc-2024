import re
import numpy as np

def part1(input: str) -> int:
    input = [x for x in input.splitlines() if x != ""]

    nrows = len(input)
    ncols = len(input[0])

    def rotate_90_deg(lst):
        rotated = []

        for j in range(nrows):
            line = []
            for i in range(ncols):
                line.append(lst[i][ncols - j - 1])
            rotated.append("".join(line))

        return rotated

    def get_all_diagonals(matrix):
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        diagonals = []

        for start_col in range(cols):
            diagonal = []
            r, c = 0, start_col
            while r < rows and c < cols:
                diagonal.append(matrix[r][c])
                r += 1
                c += 1
            diagonals.append("".join(diagonal))

        for start_row in range(1, rows):
            diagonal = []
            r, c = start_row, 0
            while r < rows and c < cols:
                diagonal.append(matrix[r][c])
                r += 1
                c += 1
            diagonals.append("".join(diagonal))

        diagonals = [diagonal for diagonal in diagonals if len(diagonal) >= len("XMAS")]

        return diagonals

    def find_xmas(lst):
        xmas_list = []

        for i, line in enumerate(lst):
            xmas_list.append((i, [x.span() for x in re.finditer(r"XMAS", line)]))

        return xmas_list

    def count_xmas(lst):
        return sum(len(matches) for _, matches in find_xmas(lst))

    count = 0
    current_input = input

    for _ in range(4):
        current_diags = get_all_diagonals(current_input)
        count += count_xmas(current_input) + count_xmas(current_diags)
        current_input = rotate_90_deg(current_input)

    return count

test_input = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

print(f"Part 1 test output = {part1(test_input)}")

with open("day4/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

def part2(input: str) -> int:
    input = [x for x in input.splitlines() if x != ""]

    nrows = len(input)
    ncols = len(input[0])

    def is_mas(lst):
        tmp = np.array([list(x) for x in lst])
        diag1 = list(np.diagonal(tmp))
        diag2 = list(np.flipud(tmp).diagonal())
        if diag1 == ["M", "A", "S"] and diag2 == ["M", "A", "S"]:
            return True
        return False

    def rotate_90_deg(lst):
        rotated = []

        nr = len(lst)
        nc = len(lst[0])

        for j in range(nr):
            line = []
            for i in range(nc):
                line.append(lst[i][nc - j - 1])
            rotated.append("".join(line))

        return rotated

    count = 0

    for r in range(nrows-2):
        for c in range(ncols-2):
            grid = [row[c:c+3] for row in input[r:r+3]]
            current_grid = grid
            for _ in range(4):
                if is_mas(current_grid):
                    count += 1
                    break
                current_grid = rotate_90_deg(current_grid)

    return count

print(f"Part 2 test output = {part2(test_input)}")

with open("day4/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")