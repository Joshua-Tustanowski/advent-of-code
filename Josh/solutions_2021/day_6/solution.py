from collections import Counter
from dataclasses import dataclass
from os.path import dirname, join
from typing import Any, List

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)

REFRESH_TIME = 6
BIRTH_TIME = 8


@dataclass
class LanternFish:
    timer: int

    def update(self) -> bool:
        reproduced = False
        self.timer -= 1
        if self.timer < 0:
            self.timer = REFRESH_TIME
            reproduced = True
        return reproduced

    @classmethod
    def create(cls) -> Any:
        return cls(timer=BIRTH_TIME)

    def __str__(self) -> str:
        return f"{self.timer}"


def parse_input(filename: str) -> List[LanternFish]:
    with open(join(CURRENT_DIR, filename), "r") as fp:
        contents = fp.read().split(",")
    initial_times = [int(t) for t in contents]
    return [LanternFish(timer=t) for t in initial_times]


def _print_lantern_fish(lantern_fish: List[LanternFish]) -> str:
    return ", ".join([str(t) for t in lantern_fish])


def part_one(file_name: str, days: int) -> int:
    lantern_fish = parse_input(file_name)
    # print(f"Initial \t {_print_lantern_fish(lantern_fish)}")
    for i in range(days):
        new_fish = []
        for fish in lantern_fish:
            can_reproduce = fish.update()
            if can_reproduce:
                new_fish.append(LanternFish.create())
        lantern_fish.extend(new_fish)
        # print(f"day {i+1} \t {_print_lantern_fish(lantern_fish)}")
    return len(lantern_fish)


def part_two_alpha(file_name: str, days: int) -> int:
    lantern_fish = parse_input(file_name)
    fish = Counter([lf.timer for lf in lantern_fish])

    for _ in range(days):
        spawn = fish[0]
        for i in range(8):
            fish[i] = fish[i + 1]
        fish[8] = spawn
        fish[6] += spawn
    return sum(fish.values())


if __name__ == "__main__":
    file = get_filename()
    result = part_one(file, days=80)
    print(f"Part one: {result=}")

    result = part_two_alpha(file, days=256)
    print(f"Part two: {result=}")
