from os.path import dirname, join
from typing import Any, Dict, List, Tuple

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)


def parse_input(file_name: str) -> List[int]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split(",")
    return [int(v) for v in contents]


def get_minimum_entry(v: Dict[int, int]) -> Tuple[int, int]:
    min_value = min(v.values())
    for key in v.keys():
        if v[key] == min_value:
            return key, v[key]
    return -1, -1


def part_one(file_name: str) -> Tuple[int, int]:
    initial_positions = parse_input(file_name)
    fuel_usages = {}
    min_pos, max_pos = min(initial_positions), max(initial_positions)
    for value in range(min_pos, max_pos + 1):
        fuel_usage = 0
        for pos in initial_positions:
            fuel_usage += abs(pos - value)
        fuel_usages[value] = fuel_usage

    return get_minimum_entry(fuel_usages)


def part_two(file_name: str) -> Tuple[int, int]:
    initial_positions = parse_input(file_name)
    fuel_usages = {}
    min_pos, max_pos = min(initial_positions), max(initial_positions)
    values = list(range(1, max_pos + 1))

    for value in range(min_pos, max_pos + 1):
        fuel_usage = 0
        for pos in initial_positions:
            val = abs(pos - value)
            fuel_usage += sum(values[:val])
        fuel_usages[value] = fuel_usage
    return get_minimum_entry(fuel_usages)


if __name__ == "__main__":
    file = get_filename()

    result = part_one(file)
    print(f"Part one: {result=}")

    result = part_two(file)
    print(f"Part two: {result=}")
