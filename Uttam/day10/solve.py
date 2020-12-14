from typing import List


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
        else:
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


def part2(inp: List[int]) -> int:
    """ Iterate through list, incrementing a same-size counter list which is tracking how many ways you can get to any
     specific number. By the end, we have the total number of ways to get to the end"""
    inp = [0] + inp
    inp = sorted(inp)
    size = len(inp)
    counts = [1] + [0 for _ in range(size - 1)]
    for n, num in enumerate(inp):
        indices_of_possible_next_nums = [i for i in range(n+1, min(n+4, size)) if 1 <= inp[i] - num <= 3]
        for j in indices_of_possible_next_nums:
            counts[j] += counts[n]

    return counts[-1]


def test_part2():
    print()
    """
    0 3 4 5
    0 3 5
    1 3 4 5
    1 3 5
    1 4 5
    """
    inp1 = load_input_file('sample4.txt')
    assert part2(inp1) == 5

    """
    0 3 4 5 7 8
    0 3 4 5 8
    0 3 4 7 8
    0 3 5 7 8
    0 3 5 8
    0 1 3 4 5 7 8 -
    0 1 3 4 5 8 -
    0 1 3 4 7 8 -
    0 1 3 5 7 8 -
    0 1 3 5 8 -
    0 1 4 5 7 8
    0 1 4 7 8
    0 1 4 5 8
    """
    inp1 = load_input_file('sample3.txt')
    assert part2(inp1) == 13

    inp1 = load_input_file('sample.txt')
    assert part2(inp1) == 8

    inp1 = load_input_file('sample2.txt')
    assert part2(inp1) == 19208
    #
    inp = load_input_file('input.txt')
    assert part2(inp) == 10578455953408
