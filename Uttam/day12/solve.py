from typing import List, Tuple
import re


def part1(inp: List[str]) -> int:
    x, y = 0, 0
    orientation = 'E'
    directions = ['N', 'E', 'S', 'W']
    for n, line in enumerate(inp, 1):
        instruction, magnitude = line[0], int(line[1:])
        if instruction == 'N':
            y += magnitude
        elif instruction == 'S':
            y -= magnitude
        elif instruction == 'E':
            x += magnitude
        elif instruction == 'W':
            x -= magnitude
        elif instruction == 'F':
            delta = {
                'N': [0, 1],
                'E': [1, 0],
                'S': [0, -1],
                'W': [-1, 0],
            }[orientation]
            x += delta[0] * magnitude
            y += delta[1] * magnitude
        elif instruction == 'L':
            assert magnitude in (90, 180, 270), f'Unknown value for turn: {line}'
            orientation = directions[int(directions.index(orientation) - (magnitude / 90))]
        elif instruction == 'R':
            assert magnitude in (90, 180, 270), f'Unknown value for turn: {line}'
            orientation = directions[(int(directions.index(orientation) + (magnitude / 90))) % 4]
    return abs(x) + abs(y)


def load_input_file(filename: str):
    with open(filename, 'r') as inp:
        return [line.strip() for line in inp.readlines()]


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 25

    inp = load_input_file('input.txt')
    assert part1(inp) == 562


def part2(inp: List[str]) -> int:
    w_x, w_y = 10, 1
    x, y = 0, 0
    for n, line in enumerate(inp, 1):
        instruction, magnitude = line[0], int(line[1:])
        if instruction == 'N':
            w_y += magnitude
        elif instruction == 'S':
            w_y -= magnitude
        elif instruction == 'E':
            w_x += magnitude
        elif instruction == 'W':
            w_x -= magnitude
        elif instruction == 'F':
            x += w_x * magnitude
            y += w_y * magnitude
        elif instruction == 'L':
            assert magnitude in (90, 180, 270), f'Unknown value for turn: {line}'
            turns = int(magnitude / 90)
            if turns == 1:
                w_x, w_y = -w_y, w_x
            elif turns == 2:
                w_x, w_y = -w_x, -w_y
            elif turns == 3:
                w_x, w_y = w_y, -w_x
        elif instruction == 'R':
            assert magnitude in (90, 180, 270), f'Unknown value for turn: {line}'
            turns = int(magnitude / 90)
            if turns == 1:
                w_x, w_y = w_y, -w_x
            elif turns == 2:
                w_x, w_y = -w_x, -w_y
            elif turns == 3:
                w_x, w_y = -w_y, w_x
    return abs(x) + abs(y)


def test_part2():
    inp1 = load_input_file('sample.txt')
    assert part2(inp1) == 286

    inp = load_input_file('input.txt')
    assert part2(inp) == 101860
