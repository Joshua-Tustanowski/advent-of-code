def open_and_parse_input(file_name):
    # [(op, value, seen), ...]
    output = []
    with open(file_name, "r") as file:
        contents = file.read()
        contents = contents.split("\n")
        for content in contents:
            operation, number = content.split(" ")
            output.append((operation, int(number), False))
    return output


def main(file_name):
    operations = open_and_parse_input(file_name)
    accumulator = 0
    i = 0
    while i < len(operations):
        print(i, operations[i])
        operation, number, seen = operations[i]
        if seen:
            break
        if operation == "acc":
            accumulator += number
        operations[i] = (operation, number, True)
        if operation == "acc" or operation == "nop":
            i += 1
        else:
            i += number
    return accumulator


if __name__ == "__main__":
    print(main("input.txt"))
