from dataclasses import dataclass
from functools import reduce
from operator import mul
from os.path import dirname, join
from typing import Dict, List, Tuple

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)

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

SIMPLE_DIRECTIONS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]


@dataclass
class Position:
    value: int
    x: int
    y: int

    def __str__(self) -> str:
        return f"Position (x={self.x}, y={self.y}) {self.value}"


def parse_input(file_name: str) -> List[List[int]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    return [[int(v) for v in c] for c in contents]


def _get_hole_positions(grid: List[List[int]]) -> List[Position]:
    hole_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbours = get_neighbours(grid, i, j)
            if grid[i][j] < min(neighbours):
                hole_positions.append(Position(x=i, y=j, value=grid[i][j]))
    return hole_positions


def get_neighbours(grid: List[List[int]], x: int, y: int) -> List[int]:
    neighbours = []
    for direction in DIRECTIONS:
        xo, yo = direction
        if (0 <= x+xo < len(grid)) and (0 <= y+yo < len(grid[x])):
            neighbours.append(grid[x+xo][y+yo])
    return neighbours


def get_neighbours_positions(grid: List[List[int]], x: int, y: int) -> List[Position]:
    neighbours = []
    for direction in SIMPLE_DIRECTIONS:
        xo, yo = direction
        xoff = x + xo
        yoff = y + yo
        if (0 <= xoff < len(grid)) and (0 <= yoff < len(grid[x])) and grid[xoff][yoff] != 9:
            neighbours.append(Position(x=xoff, y=yoff, value=grid[xoff][yoff]))
    return neighbours


def part_one(grid: List[List[int]]) -> int:
    hole_positions = _get_hole_positions(grid)
    return sum(p.value + 1 for p in hole_positions)


def _get_basin_length(grid: List[List[int]], position: Position) -> int:
    length = 1
    queue = [position]
    visited = [(position.x, position.y)]
    while queue:
        s = queue.pop(0)
        for neighbour in get_neighbours_positions(grid, s.x, s.y):
            if (neighbour.x, neighbour.y) not in visited and neighbour.value > s.value:
                visited.append((neighbour.x, neighbour.y))
                queue.append(neighbour)
                length += 1
    return length


def part_two(grid: List[List[int]]) -> int:
    hole_positions = _get_hole_positions(grid)
    basin_sizes = [_get_basin_length(grid, position) for position in hole_positions]
    return reduce(mul, sorted(basin_sizes)[-3:], 1)


if __name__ == "__main__":
    file = get_filename()
    values = parse_input(file)

    # result = part_one(values)
    # print(f"Part one: {result=}")

    result = part_two(values)
    print(f"Part two: {result=}")
