from dataclasses import dataclass
from os.path import dirname, join
from typing import List

from solutions_2021 import get_filename, TerminalColours

CURRENT_DIR = dirname(__file__)

FLASH_VALUE = 9

DIRECTIONS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
    (1, -1),
    (-1, 1),
    (-1, -1),
    (1, 1),
]


@dataclass
class Cell:
    value: int
    has_flashed: bool = False

    def __str__(self) -> str:
        if self.has_flashed:
            return f"{TerminalColours.OKGREEN}{self.value}{TerminalColours.ENDC}"
        return f"{self.value}"


@dataclass
class Grid:
    cells: List[List[Cell]]
    flashes: int = 0

    def is_synchronised(self) -> bool:
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                if self.cells[x][y].value != 0:
                    return False
        return True

    def __str__(self) -> str:
        output = [" ".join([str(col) for col in row]) for row in self.cells]  # type: ignore
        return "\n".join(output)


def parse_input(file_name: str) -> Grid:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    return Grid(cells=[[Cell(value=int(v)) for v in c] for c in contents])


def part_one(grid: Grid, steps: int = 5) -> Grid:
    for _ in range(steps):
        grid = _simulation_step(grid)
    return grid


def part_two(grid: Grid) -> int:
    counter = 0
    is_synchronised = False
    while not is_synchronised:
        grid = _simulation_step(grid)
        is_synchronised = grid.is_synchronised()
        counter += 1
    return counter


def _simulation_step(grid: Grid) -> Grid:
    for x in range(len(grid.cells)):
        for y in range(len(grid.cells[x])):
            grid.cells[x][y].value += 1

    for x in range(len(grid.cells)):
        for y in range(len(grid.cells[x])):
            grid = _flash(grid, x, y)

    for x in range(len(grid.cells)):
        for y in range(len(grid.cells[x])):
            if grid.cells[x][y].value > FLASH_VALUE:
                grid.cells[x][y].has_flashed = False
                grid.flashes += 1
                grid.cells[x][y].value = 0

    return grid


def _flash(grid: Grid, x: int, y: int) -> Grid:

    if not (grid.cells[x][y].value > FLASH_VALUE and not grid.cells[x][y].has_flashed):
        return grid

    grid.cells[x][y].has_flashed = True
    for x_off, y_off in DIRECTIONS:
        xn, yn = x + x_off, y + y_off
        if 0 <= xn < len(grid.cells) and 0 <= yn < len(grid.cells[x]):
            grid.cells[xn][yn].value += 1
            if grid.cells[xn][yn].value > FLASH_VALUE:
                grid = _flash(grid, xn, yn)
    return grid


if __name__ == "__main__":
    file = get_filename()

    values = parse_input(file)
    result_grid = part_one(values, steps=100)
    print(f"Part one: {result_grid.flashes}")

    values = parse_input(file)
    count = part_two(values)
    print(f"Part two: {count}")
