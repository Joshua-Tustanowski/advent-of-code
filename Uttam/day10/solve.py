from typing import List, Tuple
import re


def part1(inp: List[int]) -> int:
    inp = sorted(inp)
    no_of_1_jolt_diffs = 1  # at start (0 -> 1)
    no_of_3_jolt_diffs = 1  # at end (last adapter -> device)
    for i in range(len(inp) - 1):
        adapter1, adapter2 = inp[i:i+2]
        diff = adapter2 - adapter1
        assert diff in (1, 3), f'Unexpected diff for pair ({adapter1}, {adapter2}). i={i}'
        if diff == 1:
            no_of_1_jolt_diffs += 1
        elif diff == 3:
            no_of_3_jolt_diffs += 1
    return no_of_1_jolt_diffs * no_of_3_jolt_diffs


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return [int(i) for i in inp.readlines()]


def test_part1():
    print()
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 35

    inp1 = load_input_file('sample2.txt')
    assert part1(inp1) == 220

    inp = load_input_file('input.txt')
    assert part1(inp) == 1904


def find_all_paths(inp: List[int], path=None) -> List[List[int]]:
    if path is None:
        path = []
    path = path + [inp[0]]
    if len(inp) == 1:
        return [path]

    paths = []
    for i in range(len(inp)):
        a = inp[i]
        print(f'i={i}, inp={inp}')
        possible_next_joltage_indices = [j for j in range(i+1, min(i+4, len(inp))) if 1 <= inp[j] - a <= 3]
        # ps = []
        for j in possible_next_joltage_indices:
            onward_paths = find_all_paths(inp[j:], path)
            for path in onward_paths:
                paths.append(path)
        # paths.extend(ps)
    return paths


def part2(inp: List[int]) -> int:
    inp = sorted(inp)
    paths = find_all_paths(inp)
    import pdb; pdb.set_trace()
    return len(paths)


def test_part2():
    print()
    inp1 = load_input_file('sample.txt')
    assert part2(inp1) == 8

    inp1 = load_input_file('sample2.txt')
    assert part2(inp1) == 19208

    inp = load_input_file('input.txt')
    assert part2(inp) == None
