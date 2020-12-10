from pathlib import Path

file = Path('input/test2.txt')

data = sorted([int(line) for line in file.open('r')])

one_diffs, three_diffs = 0, 0
for i in range(len(data)-1):
    for addition in range(1, 4):
        if data[i] + addition == data[i+1]:
            if addition == 3:
                three_diffs += 1
            elif addition == 1:
                one_diffs += 1

print(data)
print('od:', one_diffs, 'td:', three_diffs)
print(one_diffs * three_diffs)  # Wrong ?

one_diffs, three_diffs = 0, 0
for i in range(len(data)-1):
    diff = data[i+1] - data[i]
    if diff == 1:
        one_diffs += 1
    elif diff == 3:
        three_diffs += 1

print(data)
print('od:', one_diffs, 'td:', three_diffs)
print(one_diffs * three_diffs)  # Wrong ?
