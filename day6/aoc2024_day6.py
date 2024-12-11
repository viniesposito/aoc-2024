# imports

# part 1 code
def part1(input: str) -> int:
    input = [x for x in input.splitlines() if x != ""]

    guard_dict = {
        "^":(-1,0),
        ">":(0,1),
        "v":(1,0),
        "<":(0,-1)
    }

    rotate_dict = {
        (-1,0):(0,1),
        (0,1):(1,0),
        (1,0):(0,-1),
        (0,-1):(-1,0)
    }

    guards = guard_dict.keys()

    def get_current_guard(grid):
        for g in guards:
            idx = "".join(grid).find(g)
            if idx > -1:
                return (int(idx / len(grid)), idx % len(grid)), guard_dict[g]
            
    def get_next_stop(current_pos, travel_dir):
        return current_pos[0] + travel_dir[0], current_pos[1] + travel_dir[1]

    def is_stop_good(pos):
        x, y= pos
        if (not (0<=x<=len(input)-1)) or (not (0<=y<=len(input[0])-1)):
            return True
        return input[x][y] != "#"

    pos, direction = get_current_guard(input)

    visited = [pos]
    next_x, next_y = get_next_stop(pos, direction)

    while 0<next_x<len(input) and 0<next_y<len(input[0]):
        potential_pos = get_next_stop(pos, direction)

        if not is_stop_good(potential_pos):
            new_direction = rotate_dict[direction]
            potential_pos = get_next_stop(pos, new_direction)
            if not is_stop_good(get_next_stop(pos, new_direction)):
                while not is_stop_good(potential_pos):
                    new_direction = rotate_dict[direction]
                    potential_pos = get_next_stop(pos, new_direction)
            direction = new_direction

        pos = potential_pos
        visited.append(pos)
        next_x, next_y = pos

    return len(set(visited)) - 1

test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

# part 1 outputting
print(f"Part 1 test output = {part1(test_input)}")

with open("day6/input", "r") as input:
    print(f"Part 1 output = {part1(input.read())}")

# part 2 code
def part2(input: str) -> int:
    pass

# part 2 outputting
print(f"Part 2 test output = {part2(test_input)}")

with open("day6/input", "r") as input:
    print(f"Part 2 output = {part2(input.read())}")