def read_and_parse_input(file_name: str) -> list:
    with open(file_name, "r") as file:
        contents = file.read()
        contents = contents.split("\n")
    for i, content in enumerate(contents):
        contents[i] = int(content)
    return contents


def populate_possible_sums(numbers, preamble, start=0):
    sums = set()
    for i in range(start - preamble, start):
        for j in range(i + 1, start):
            sums.add(numbers[i] + numbers[j])
    return list(sums)


def search_for_groups(numbers, invalid):
    i = 0
    while i < len(numbers):
        if i + 1 < len(numbers) and numbers[i] < invalid:
            j = i + 1
            sum_ = numbers[i]
            while j < len(numbers) and sum_ <= invalid:
                if sum_ == invalid:
                    return i, j - 1
                    break
                sum_ += numbers[j]
                j += 1
        if sum_ == invalid:
            break
        i += 1
    return -1, -1


def check_encryption(numbers, preamble):
    for i in range(preamble, len(numbers)):
        sums = populate_possible_sums(numbers, preamble=preamble, start=i)
        if numbers[i] not in sums:
            break
    return numbers[i]


if __name__ == "__main__":
    preamble = 25
    numbers = read_and_parse_input("input.txt")
    invalid = check_encryption(numbers, preamble)
    i, j = search_for_groups(numbers, invalid)
    if i != -1 and j != -1:
        nums = numbers[i : j + 1]
        min_ = min(nums)
        max_ = max(nums)
        print(min_, max_, min_ + max_)
