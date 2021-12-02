from typing import List


def solution(values: List[int], rounds: int) -> int:
    numbers = {num: i + 1 for i, num in enumerate(values)}
    prev = nums[-1]
    for turn in range(len(values) + 1, rounds + 1):
        if prev not in numbers:
            num = 0
        else:
            num = turn - 1 - numbers[prev]
        numbers[prev] = turn - 1
        prev = num
    return prev


if __name__ == "__main__":
    nums = [12, 1, 16, 3, 11, 0]
    print(solution(nums, 30000000))
