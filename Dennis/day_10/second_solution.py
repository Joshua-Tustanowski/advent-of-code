from pathlib import Path
from collections import Counter


def solve(list_of_ints) -> int:
    counter = Counter({0: 1})
    for x in data:
        counter[x+1] += counter[x]
        counter[x+2] += counter[x]
        counter[x+3] += counter[x]

    return counter[max(data) + 3]  # ans: 1727094849536


def solve_combinatorics(list_of_ints):
    list_of_ints += [list_of_ints[-1] + 3]
    counter = Counter({1: 0})
    consecutive_one_diff = -1
    for i in range(len(data)-1):
        if (next_point := data[i+1]) - (this_point := data[i]) > 2:
            if consecutive_one_diff > 0:
                counter[consecutive_one_diff] += 1
            consecutive_one_diff = -1
        else:
            consecutive_one_diff += 1

    mapper = {
        1: 2,
        2: 4,
        3: 7,
        4: 11
    }

    answer = 1
    for key in mapper.keys():
        answer *= mapper[key] ** counter[key]

    return answer  # ans: 1727094849536


if __name__ == '__main__':
    file = Path('input/data2.txt')
    data = sorted([0] + [int(line) for line in file.open('r')])
    print(solve(data))
    print(solve_combinatorics(data))
