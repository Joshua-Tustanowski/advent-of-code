import re
from collections import defaultdict
from dataclasses import dataclass
from os.path import dirname, join
from typing import Dict, List, Tuple

from solutions_2021 import get_filename, TerminalColours

CURRENT_DIR = dirname(__file__)


@dataclass
class Instruction:
    direction: str = "x"
    axis: int = -1


@dataclass
class Cell:
    x: int
    y: int
    marked: bool = False
    flipping: bool = False

    def __str__(self) -> str:
        ret = "#" if self.marked else "."
        if self.flipping:
            return f"{TerminalColours.OKGREEN}{ret}{TerminalColours.ENDC}"
        return ret


class Grid:
    def __init__(self, cells: List[Cell]):
        max_x = max([cell.x for cell in cells])
        max_y = max([cell.y for cell in cells])
        self.cells = [[Cell(x=x, y=y) for x in range(max_x + 1)] for y in range(max_y + 1)]
        for cell in cells:
            self.cells[cell.y][cell.x] = cell

    def marked_cells(self):
        return [[self.cells[x][y].marked for y in range(len(self.cells[x]))] for x in range(len(self.cells))]

    def fold(self, instruction: Instruction):
        if instruction.direction == "y":
            for x in range(len(self.cells)):
                for y in range(len(self.cells[x])):
                    if x >= instruction.axis and self.cells[x][y].marked:
                        new_x = abs(x - instruction.axis)
                        x_pos = instruction.axis - new_x
                        self.cells[x_pos][y].marked = True
            cells = [
                [self.cells[x][y] for y in range(len(self.cells[0]))]
                for x in range(len(self.cells))
                if x < instruction.axis
            ]
            self.cells = cells
            # get all cells below the vertical line
        elif instruction.direction == "x":
            for x in range(len(self.cells)):
                for y in range(len(self.cells[x])):
                    if y >= instruction.axis and self.cells[x][y].marked:
                        new_y = abs(y - instruction.axis)
                        y_pos = instruction.axis - new_y
                        self.cells[x][y_pos].marked = True
            cells = [
                [self.cells[x][y] for y in range(len(self.cells[0])) if y < instruction.axis]
                for x in range(len(self.cells))
            ]
            self.cells = cells

    def __str__(self) -> str:
        output = [" ".join([str(col) for col in row]) for row in self.cells]  # type: ignore
        return "\n".join(output)


def parse_input(file_name: str) -> Tuple[Grid, List[Instruction]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        positions, axes = fp.read().split("\n\n")
    cells = []
    for position in positions.split("\n"):
        start, end = position.split(",")
        cells.append(Cell(marked=True, x=int(start), y=int(end)))
    grid = Grid(cells=cells)
    instr = []
    pattern = re.compile(r"fold along ([x-y])=(\d+)")
    for instruction in axes.split("\n"):
        matched = re.match(pattern, instruction)
        instr.append(Instruction(direction=matched.group(1), axis=int(matched.group(2))))
    return grid, instr


def part_one(cells: Grid, instruction: Instruction) -> int:
    cells.fold(instruction)
    marked_cells = cells.marked_cells()
    counter = 0
    for row in marked_cells:
        counter += sum(row)
    return counter


def part_two(cells: Grid, instructions: List[Instruction]) -> Grid:
    for instruction in instructions:
        cells.fold(instruction)
    return cells


if __name__ == "__main__":
    file = get_filename()
    grid, instructions = parse_input(file)
    result = part_one(grid, instruction=instructions[0])
    print(result)

    result = part_two(grid, instructions)
    print(grid)
