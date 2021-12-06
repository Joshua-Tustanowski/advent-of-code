from dataclasses import dataclass
from enum import Enum
from os.path import dirname, join
from typing import List, Tuple

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)


class TerminalColours(str, Enum):
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def __str__(self) -> str:
        return self.value


@dataclass
class Cell:
    value: int
    seen: bool = False

    def __str__(self) -> str:
        if self.seen:
            return f"{TerminalColours.OKGREEN}{self.value}{TerminalColours.ENDC}"
        return f"{self.value}"


@dataclass
class Grid:
    cells: List[List[Cell]]
    width: int = 5
    height: int = 5
    has_bingo: bool = False

    def print(self) -> None:
        output = [" ".join([str(col) for col in row]) for row in self.cells]  # type: ignore
        print("\n".join(output))

    def mark(self, value: int) -> None:
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[y][x]
                if cell.value == value:
                    cell.seen = True

    def is_bingo(self) -> bool:
        def _is_bingo_x(cells: List[List[Cell]], x: int, y: int) -> bool:
            if x >= self.height:
                return True

            cell = cells[x][y]
            is_seen = cell.seen

            return is_seen and _is_bingo_x(cells, x + 1, y)

        def _is_bingo_y(cells: List[List[Cell]], x: int, y: int) -> bool:
            if y >= self.height:
                return True

            cell = cells[x][y]
            is_seen = cell.seen

            return is_seen and _is_bingo_y(cells, x, y + 1)

        for x in range(self.width):
            if _is_bingo_y(self.cells, x, 0):
                return True

        for y in range(self.width):
            if _is_bingo_x(self.cells, 0, y):
                return True

        return False

    def unmarked(self) -> List[int]:
        unseen_values = []
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[y][x]
                if not cell.seen:
                    unseen_values.append(cell.value)
        return unseen_values


def parse_input(filename: str) -> Tuple[List[int], List[Grid]]:
    with open(join(CURRENT_DIR, filename), "r") as fp:
        contents = fp.read().split("\n\n")

    order = [int(val) for val in contents[0].split(",")]

    grids = []
    for grid in contents[1:]:
        rows = grid.split("\n")
        cells = []
        for row in rows:
            columns = [int(val) for val in row.split(" ") if val]
            cells.append([Cell(value=col) for col in columns])
        cgrid = Grid(cells=cells)
        grids.append(cgrid)
    return order, grids


def part_one(filename: str) -> int:
    orders, grids = parse_input(filename)
    is_bingo = False
    last_order, last_grid = orders[0], grids[0]

    for order in orders:
        for grid in grids:
            grid.mark(order)
            if grid.is_bingo():
                last_grid = grid
                is_bingo = True
        if is_bingo:
            last_order = order
            break
    return sum(last_grid.unmarked()) * last_order


def part_two(filename: str) -> int:
    orders, grids = parse_input(filename)
    last_order, losing_grid = orders[0], grids[0]

    for order in orders:
        for grid in grids:
            if grid.has_bingo:
                continue
            grid.mark(order)
            if grid.is_bingo():
                grid.has_bingo = True
                last_order, losing_grid = order, grid

    return sum(losing_grid.unmarked()) * last_order


if __name__ == "__main__":
    file = get_filename()

    result = part_one(file)
    print(f"Part one: {result=}")

    result = part_two(file)
    print(f"Part one: {result=}")
