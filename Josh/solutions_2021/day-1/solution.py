from os.path import dirname, join
from typing import List

from solutions_2021 import DEBUG

current_dir = dirname(__file__)


def parse_file(filename: str) -> List[int]:
    with open(join(current_dir, filename), "r") as fp:
        contents = fp.read()
    return [int(val) for val in contents.split("\n")]


def part_one(file_name: str) -> int:
    values = parse_file(file_name)
    return _get_increasing_count(values)


def _get_increasing_count(values: List[int]) -> int:
    prev, count = values[0], 0
    for i in range(1, len(values)):
        if values[i] > prev:
            count += 1
        prev = values[i]
    return count


def part_two(file_name: str, window_size: int = 3) -> int:
    values = parse_file(file_name)
    return _get_increasing_count([sum(values[i : i + window_size]) for i in range((len(values) - window_size + 1))])


if __name__ == "__main__":
    file = "basic-input.txt" if not DEBUG else "sample-input.txt"

    result = part_one(file)
    print(f"Part one: {result=}")

    result = part_two(file)
    print(f"Part two: {result=}")
