from collections import Counter
from os.path import dirname, join
from typing import List, Tuple

import pandas as pd

from solutions_2021 import DEBUG

CURRENT_DIR = dirname(__file__)


def parse_file(file_name: str) -> pd.DataFrame:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    separated = [[c for c in entry] for entry in contents]
    return pd.DataFrame(separated)


def _bin_to_decimal(binary: str) -> int:
    value = 0
    for i, val in enumerate(binary):
        value += int(val) * (2 ** (len(binary) - i - 1))
    return value


def part_one(file_name: str) -> int:
    df = parse_file(file_name)
    g_vals, e_vals = [], []
    for col in df:
        values = df[col].value_counts()
        mask = values == values.max()
        max_ = values[mask]
        min_ = values[~mask]
        g_vals.append(max_.index[0])
        e_vals.append(min_.index[0])
    gamma = _bin_to_decimal("".join(g_vals))
    epsilon = _bin_to_decimal("".join(e_vals))
    return gamma * epsilon


def part_two(file_name: str) -> int:
    input_df = parse_file(file_name)
    size = len(input_df.columns)

    def _generator(df: pd.DataFrame, idx: int, default: str):
        if len(df) == 1:
            return df
        values = df[idx].value_counts()
        if default == "0":
            extreme = values[values == values.min()]
        else:
            extreme = values[values == values.max()]
        extreme_value = default if len(extreme) > 1 else extreme.index[0]
        tmp = df[df[idx] == extreme_value]
        return _generator(tmp, (idx + 1) % size, default)

    oxygen = _generator(input_df, 0, "1")
    scrubber = _generator(input_df, 0, "0")
    sc_val = _bin_to_decimal("".join(scrubber.iloc[-1].tolist()))
    ox_val = _bin_to_decimal("".join(oxygen.iloc[-1].tolist()))
    return sc_val * ox_val


if __name__ == "__main__":
    file = "basic-input.txt" if not DEBUG else "sample-input.txt"

    result = part_one(file)
    print(f"Part one: {result=}")

    result = part_two(file)
    print(f"Part two: {result=}")
