cups = "952438716"
cups = [int(cup) for cup in cups]
SIZE = len(cups)


def remove_three_cups(cups, current_cup):
    idx = cups.index(current_cup)
    res = []
    if idx + 3 < SIZE - 1:
        for _ in range(3):
            res.append(cups.pop(idx + 1))
    elif idx == SIZE - 1:
        for _ in range(3):
            res.append(cups.pop(0))
    else:
        diff = SIZE - 1 - idx
        for _ in range(diff):
            res.append(cups.pop(idx + 1))
        for _ in range(3 - diff):
            res.append(cups.pop(0))
    return res


def game_round(cups, current_cup):
    # 1. pick up the three cups immediately clockwise of the current cup
    removed_cups = remove_three_cups(cups, current_cup)

    # 2. Destination cup
    destination = current_cup - 1
    while destination not in cups:
        destination -= 1
        if destination <= 0:
            destination = max(cups)
    tmp_cup = current_cup
    idx = cups.index(current_cup)
    while tmp_cup != destination:
        tmp_cup = cups[idx]
        idx += 1
        idx = idx % 6

    cups = cups[:idx] + removed_cups + cups[idx:]
    current_cup = cups[(cups.index(current_cup) + 1) % SIZE]
    return cups, current_cup


def get_result_string(cups):
    idx = (cups.index(1) + 1) % len(cups)
    ret = ""
    for _ in range(len(cups) - 1):
        ret += str(cups[idx])
        idx = (idx + 1) % len(cups)
    return ret


def part_two(nums):
    cups = {}
    prev = None
    for i in range(len(nums) - 1, -1, -1):
        cups[nums[i]] = prev
        prev = nums[i]
    for i in range(int(1e6), 9, -1):
        cups[i] = prev
        prev = i

    cups[nums[-1]] = 10
    cur = nums[0]

    for _ in range(int(1e7)):
        remove1 = cups[cur]
        remove2 = cups[remove1]
        remove3 = cups[remove2]
        cups[cur] = cups[remove3]

        removed = {cur, remove1, remove2, remove3}
        cval = cur
        while cval in removed:
            cval -= 1
            if cval == 0:
                cval = int(1e6)
        targetLoc = cval
        afterTarget = cups[targetLoc]
        cups[cval] = remove1
        cups[remove3] = afterTarget
        cur = cups[cur]

    return cups[1] * cups[cups[1]]


if __name__ == "__main__":
    # cup = 9
    # for _ in range(100):
    #     cups, cup = game_round(cups, cup)
    # print(get_result_string(cups))
    print(part_two(cups))
