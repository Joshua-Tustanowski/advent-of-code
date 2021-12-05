import re
from typing import List, Tuple


def part1(inp: List[str]) -> int:
    earliest_time = int(inp[0])
    bus_ids = [int(bus_id) for bus_id in inp[1].split(",") if bus_id.isdigit()]
    wait_times = [(bus_id, bus_id * (earliest_time // bus_id) + bus_id - earliest_time) for bus_id in bus_ids]
    best_bus = sorted(wait_times, key=lambda x: x[1])[0]
    return best_bus[0] * best_bus[1]


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    inp1 = load_input_file("sample.txt")
    assert part1(inp1) == 295

    inp = load_input_file("input.txt")
    assert part1(inp) == 4135


def part2(inp: str) -> int:
    bus_ids = [(n, int(bus_id)) for n, bus_id in enumerate(inp.split(",")) if bus_id != "x"]
    pass


def test_part2():
    my_sample = "7,13"
    assert part2(my_sample) == 77

    # extra_sample1 = '17,x,13,19'
    # assert part2(extra_sample1) == 3417

    # inp1 = load_input_file('sample.txt')
    # assert part2(inp1) == 1068781

    # inp = load_input_file('input.txt')
    # assert part2(inp) == None
