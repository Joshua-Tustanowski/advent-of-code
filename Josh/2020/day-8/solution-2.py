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


def loop_over(operations):
    accumulator = 0
    i = 0
    while i < len(operations):
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
    return accumulator, seen


def find_all_jmps(operations):
    jmps = []
    for i, operation in enumerate(operations):
        op, _, _ = operation
        if op == "jmp":
            jmps.append(i)
    return jmps


def main(file_name):
    operations = open_and_parse_input(file_name)
    jmp_position = find_all_jmps(operations)
    for jmp in jmp_position:
        op, number, seen = operations[jmp]
        operations[jmp] = ("nop", number, seen)
        print(jmp, operations[jmp])
        acc, seen = loop_over(operations)
        for i in range(len(operations)):
            op, num, _ = operations[i]
            operations[i] = (op, num, False)
        operations[jmp] = ("jmp", number, seen)
        if seen == False:
            return acc


if __name__ == "__main__":
    print(main("input.txt"))
