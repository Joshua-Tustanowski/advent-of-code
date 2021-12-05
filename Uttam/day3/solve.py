import re
from collections import Counter
from typing import List, Tuple


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return inp.read().splitlines() if lines else inp.read()


def calculate_trees_encountered(area_map: List[List[str]], slope_x: int, slope_y: int) -> int:
    _width = len(area_map[0])
    x, y = 0, 0
    trees_encountered = 0
    while y < len(area_map) - 1:
        x, y = (x + slope_x) % _width, y + slope_y
        if area_map[y][x] == "#":
            trees_encountered += 1
    return trees_encountered


def part1(area_map: List[List[str]]) -> int:
    return calculate_trees_encountered(area_map, 3, 1)


def test_part1():
    map1 = load_input_file("map1.txt")
    assert calculate_trees_encountered(map1, 3, 1) == 7

    inp = load_input_file("input.txt", lines=True)
    assert calculate_trees_encountered(inp, 3, 1) == 254


def part2(area_map: List[List[str]]) -> int:
    product = 1
    for slope_x, slope_y in [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]:
        trees = calculate_trees_encountered(area_map, slope_x, slope_y)
        product *= trees
    return product


def test_calculate_trees_encountered():
    map1 = load_input_file("map1.txt")
    assert calculate_trees_encountered(map1, 1, 1) == 2
    assert calculate_trees_encountered(map1, 3, 1) == 7
    assert calculate_trees_encountered(map1, 5, 1) == 3
    assert calculate_trees_encountered(map1, 7, 1) == 4
    assert calculate_trees_encountered(map1, 1, 2) == 2


def test_part2():
    map1 = load_input_file("map1.txt")
    assert part2(map1) == 336

    test_map = load_input_file("input.txt")
    assert part2(test_map) == 0
