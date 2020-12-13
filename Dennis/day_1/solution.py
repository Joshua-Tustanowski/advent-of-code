from pathlib import Path


def solve(input):
    for i in range(len(input)):
        this = input[i]
        for j in range(i, len(input)):
            following = input[j]
            if this + following == 2020:
                return this * following

    return 0


def solve_two(input):
    for i in range(len(input)):
        this = input[i]
        for j in range(i, len(input)):
            following = input[j]
            for w in range(j, len(input)):
                after_following = input[w]
                if this + following + after_following == 2020:
                    return this * following * after_following

    return 0


if __name__ == '__main__':
    file = Path('data.txt')
    data = [int(x) for x in file.open('r')]
    print(solve(data))
    b = Path('data2.txt')
    db = [int(x) for x in b.open('r')]
    print(solve_two(db))
