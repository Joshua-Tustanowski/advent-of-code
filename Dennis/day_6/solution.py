from pathlib import Path

with Path("input/6.txt").open("r") as file:
    content = file.read()

data = content.split("\n\n")

count = 0
for group in data:
    group = group.replace("\n", "")
    group = "".join(set(group))
    count += len(group)

print(count)
