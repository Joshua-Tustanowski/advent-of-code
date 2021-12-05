import re
from typing import List, Tuple


def get_adjacent_coords(row: int, col: int, map_: List[List[str]]) -> List[Tuple[int, int]]:
    """
    1 2 3
    4 X 5
    6 7 8
    """
    height = len(map_)
    width = len(map_[0])
    row_above = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
    row_curr = [(row, col - 1), (row, col + 1)]
    row_below = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    adjacent_coords = []
    for coord_x, coord_y in row_above + row_curr + row_below:
        if coord_x in range(0, height) and coord_y in range(0, width):
            adjacent_coords.append((coord_x, coord_y))

    return adjacent_coords


def no_of_occupied_seats_all_around(row: int, col: int, map_: List[List[str]]) -> int:
    height = len(map_)
    width = len(map_[0])
    total = 0
    # todo - horribly violates DRY
    # Top left
    test_x, test_y = col, row
    while True:
        if test_x == 0 or test_y == 0:
            break
        test_x -= 1
        test_y -= 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Above
    test_x, test_y = col, row
    while True:
        if test_y == 0:
            break
        test_y -= 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Top right
    test_x, test_y = col, row
    while True:
        if test_x == width - 1 or test_y == 0:
            break
        test_x += 1
        test_y -= 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Left
    test_x, test_y = col, row
    while True:
        if test_x == 0:
            break
        test_x -= 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Right
    test_x, test_y = col, row
    while True:
        if test_x == width - 1:
            break
        test_x += 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Bottom left
    test_x, test_y = col, row
    while True:
        if test_x == 0 or test_y == height - 1:
            break
        test_x -= 1
        test_y += 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Below
    test_x, test_y = col, row
    while True:
        if test_y == height - 1:
            break
        test_y += 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    # Bottom right
    test_x, test_y = col, row
    while True:
        if test_x == width - 1 or test_y == height - 1:
            break
        test_x += 1
        test_y += 1
        test_seat = map_[test_y][test_x]
        if test_seat == "#":
            total += 1
            break
        elif test_seat == "L":
            break

    return total


def part1(map_: List[List[str]]) -> int:
    print("\n")
    print(len(map_))
    print(len(map_[0]))
    counter = 0
    while True:
        counter += 1
        next_map = []
        for row_n, row in enumerate(map_):
            new_row = []
            for col_n in range(len(row)):
                current_seat = map_[row_n][col_n]
                if current_seat == "L":
                    occupied_seats_around = 0
                    for r, c in get_adjacent_coords(row_n, col_n, map_):
                        if map_[r][c] == "#":
                            occupied_seats_around += 1
                    if occupied_seats_around == 0:
                        new_seat = "#"
                    else:
                        new_seat = current_seat

                elif current_seat == "#":
                    occupied_seats_around = 0
                    for r, c in get_adjacent_coords(row_n, col_n, map_):
                        if map_[r][c] == "#":
                            occupied_seats_around += 1
                    if occupied_seats_around >= 4:
                        new_seat = "L"
                    else:
                        new_seat = current_seat
                else:
                    new_seat = current_seat
                new_row.append(new_seat)
            next_map.append(new_row)

        if next_map == map_:
            break
        else:
            map_ = next_map

    no_of_occupied_seats_in_steady_state = 0
    for row in map_:
        for seat in row:
            if seat == "#":
                no_of_occupied_seats_in_steady_state += 1
    return no_of_occupied_seats_in_steady_state


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return [l.strip() for l in inp.readlines()]


def test_part1():
    inp1 = load_input_file("sample.txt")
    assert len(get_adjacent_coords(0, 0, inp1)) == 3
    assert len(get_adjacent_coords(2, 3, inp1)) == 8
    assert len(get_adjacent_coords(9, 4, inp1)) == 5

    assert part1(inp1) == 37

    inp = load_input_file("input.txt")
    assert part1(inp) == 2249


def part2(map_: List[str]) -> int:
    counter = 0
    while True:
        counter += 1
        next_map = []
        for row_n, row in enumerate(map_):
            new_row = []
            for col_n in range(len(row)):
                current_seat = map_[row_n][col_n]
                no_of_occupied_seats_around = no_of_occupied_seats_all_around(row_n, col_n, map_)
                if current_seat == "L":
                    if no_of_occupied_seats_around == 0:
                        new_seat = "#"
                    else:
                        new_seat = current_seat
                elif current_seat == "#":
                    if no_of_occupied_seats_around >= 5:
                        new_seat = "L"
                    else:
                        new_seat = current_seat
                else:
                    new_seat = current_seat
                new_row.append(new_seat)
            next_map.append(new_row)

        if next_map == map_:
            break
        else:
            map_ = next_map

    no_of_occupied_seats_in_steady_state = 0
    for row in map_:
        for seat in row:
            if seat == "#":
                no_of_occupied_seats_in_steady_state += 1
    return no_of_occupied_seats_in_steady_state


def test_part2():
    inp1 = load_input_file("sample.txt")
    assert part2(inp1) == 26

    inp = load_input_file("input.txt")
    assert part2(inp) == 2023
