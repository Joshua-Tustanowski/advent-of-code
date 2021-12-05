import re
from typing import Callable, List, Tuple


class GameBoy:
    def __init__(self, inp: List[str], jmp_to_change: int = None):
        self.inp = inp
        self.pointer = 0
        self.accumulator = 0
        self.visited_pointers = set()
        self.jmp_to_change = jmp_to_change
        self.jmp_counter = 0

    def run(self):
        while True:
            if self.pointer >= len(self.inp):
                break

            if self.pointer in self.visited_pointers:
                # print('Previous pointer {} encountered {}'.format(self.pointer, self.visited_pointers))
                return False, self.accumulator

            line = self.inp[self.pointer]
            self.visited_pointers.add(self.pointer)
            func, arg = self.parse_line(line)
            # print(f'[{self.pointer}] Running {func} with arg {arg}')
            func(arg)
        print("Program ran successfully. Accumulator: {}".format(self.accumulator))
        return True, self.accumulator

    def parse_line(self, line: str) -> Tuple[Callable, int]:
        func = None
        if "acc" in line:
            func = self.acc
        elif "jmp" in line:
            if self.jmp_to_change == self.jmp_counter:
                print("Changing jmp #{} to nop".format(self.jmp_to_change))
                func = self.nop
            else:
                func = self.jmp
            self.jmp_counter += 1
        elif "nop" in line:
            func = self.nop
        assert func is not None, f"No func for {line}"
        arg = int(line[4:])
        return func, arg

    def acc(self, arg):
        self.accumulator += arg
        self.pointer += 1

    def jmp(self, arg):
        self.pointer += arg

    def nop(self, arg):
        self.pointer += 1


def part1(inp: List[str]) -> int:
    gb = GameBoy(inp)
    _, accum = gb.run()
    return accum


def part2(inp: List[str]) -> int:
    nop_to_change = 0
    while True:
        gb = GameBoy(inp, nop_to_change)
        success, accum = gb.run()
        if success:
            return accum
        nop_to_change += 1


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return inp.read().splitlines() if lines else inp.read()


def test_part1():
    inp1 = load_input_file("sample.txt")
    assert part1(inp1) == 5

    inp = load_input_file("input.txt")
    assert part1(inp) == 1586


def test_part2():
    inp1 = load_input_file("sample.txt")
    assert part2(inp1) == 8

    inp = load_input_file("input.txt")
    assert part2(inp) == 703
