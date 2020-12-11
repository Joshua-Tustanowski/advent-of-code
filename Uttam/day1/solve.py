from typing import List


def load_input_file(filename: str, lines: bool = True) -> str:
    with open(filename, 'r') as inp:
        return inp.readlines() if lines else inp.read()


def part1(inp: List[str]) -> int:
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            a, b = int(inp[i]), int(inp[j])
            if a + b == 2020:
                return a * b


def test_part1():
    inp1 = """1721
979
366
299
675
1456""".splitlines()
    assert part1(inp1) == 514579

    inp = load_input_file('input.txt', lines=True)
    assert part1(inp) == 964875


def part2(inp: List[str]) -> int:
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            for k in range(j, len(inp)):
                a, b, c = int(inp[i]), int(inp[j]), int(inp[k])
                if a + b + c == 2020:
                    return a * b * c


def test_part2():
    inp1 = """1721
979
366
299
675
1456""".splitlines()
    assert part2(inp1) == 241861950

    inp = load_input_file('input.txt', lines=True)
    assert part2(inp) == 158661360
