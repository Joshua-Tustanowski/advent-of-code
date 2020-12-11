from typing import List


def read_and_parse_input(file_name: str) -> list:
    with open(file_name, 'r') as _input:
        _input = _input.read()
        _input = _input.split('\n')
    for i in range(len(_input)):
        _input[i] = int(_input[i])
    return _input


def form_joltages(file_name):
    values = read_and_parse_input(file_name)
    max_joltage = max(values) + 3
    values.append(max_joltage)
    values = [0] + values
    return values


def part_one(values):
    diffs = {1: 0, 2: 0, 3: 0}
    values.sort()
    val = values[0]
    for i in range(1, len(values)):
        diff = values[i] - val
        if diff <= 3:
            diffs[diff] += 1
            val = values[i]
        else:
            break
    return diffs[1] * diffs[3]


def combinations(joltages: List[int]) -> int:
    route_lengths = {0: 1}
    for joltage in joltages:
        total_routes = 0
        for n in [1, 2, 3]:
            total_routes += route_lengths.get(joltage - n, 0)
        route_lengths[joltage] = total_routes
    return route_lengths[joltages[-1]]


if __name__ == "__main__":
    values = form_joltages('input.txt')
    # ------- part 1 ------- #
    res = part_one(values)
    assert res == 2312
    # ------- part 2 ------- #
    res = combinations(values[1:])
    assert res == 12089663946752