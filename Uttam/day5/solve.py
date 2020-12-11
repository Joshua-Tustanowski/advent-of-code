from typing import List, Tuple
import re
from math import floor, ceil
from collections import Counter


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.read().splitlines() if lines else inp.read()


def binary_space_partitioning(chars: str, low: int, high: int) -> int:
    print(f'Start ({chars}) ({low}, {high})')
    for char in chars:
        print()
        if char == 'F':
            print('Char is F')
            high = low + floor((high - low) / 2)
        else:
            print('Char is B')
            low = low + ceil((high - low) / 2)
        print(f'{low}, {high}')
    assert low == high, f'By now low and high should be the same: ({low}, {high})'
    return low


def determine_row_number(chars: str) -> int:
    assert len(chars) == 7
    low, high = 0, 127
    # print(f'Start ({chars}) ({low}, {high})')
    for char in chars:
        # print()
        if char == 'F':
            # print('Char is F')
            high = low + floor((high - low) / 2)
        else:
            # print('Char is B')
            low = low + ceil((high - low) / 2)
        # print(f'{low}, {high}')
    assert low == high, f'By now low and high should be the same: ({low}, {high})'
    return low


def determine_column_number(chars: str) -> int:
    assert len(chars) == 3
    low, high = 0, 7
    # print(f'Start ({chars}) ({low}, {high})')
    for char in chars:
        # print()
        # print(f'Char is {char}')
        if char == 'L':
            high = low + floor((high - low) / 2)
        else:
            low = low + ceil((high - low) / 2)
        # print(f'{low}, {high}')
    assert low == high, f'By now low and high should be the same: ({low}, {high})'
    return low


def parse_seat_location(chars: str) -> Tuple[int, int]:
    assert len(chars) == 10
    row = determine_row_number(chars[:7])
    col = determine_column_number(chars[7:])
    return row, col


def calculate_seat_id(row: int, col: int) -> int:
    return 8 * row + col


def part1(boarding_passes: List[str]) -> int:
    seat_ids = []
    for boarding_pass in boarding_passes:
        row, col = parse_seat_location(boarding_pass)
        seat_ids.append(calculate_seat_id(row, col))
    return max(seat_ids)


def test_part1():
    assert parse_seat_location('FBFBBFFRLR') == (44, 5)
    assert parse_seat_location('BFFFBBFRRR') == (70, 7)
    assert parse_seat_location('FFFBBBFRRR') == (14, 7)
    assert parse_seat_location('BBFFBBFRLL') == (102, 4)

    inp1 = load_input_file('input.txt')
    assert part1(inp1) == 933


def part2(boarding_passes: List[str]) -> int:
    seat_map = [[0 for _ in range(8)] for _ in range(128)]
    for boarding_pass in boarding_passes:
        row, col = parse_seat_location(boarding_pass)
        seat_map[row][col] = 1

    # Display map
    for row_n, row in enumerate(seat_map):
        print('{:3} {}'.format(row_n, row))

    rows_with_only_one_missing_seat = [(row_n, row) for row_n, row in enumerate(seat_map) if Counter(row)[0] == 1]
    print('\nRows with only 1 missing seat:')
    assert len(rows_with_only_one_missing_seat) == 1, f'Multiple rows found with only 1 missing seat'
    [row_n, row] = rows_with_only_one_missing_seat[0]
    col = row.index(0)
    return calculate_seat_id(row_n, col)


def test_part2():
    inp1 = load_input_file('input.txt')
    assert part2(inp1) == 711
