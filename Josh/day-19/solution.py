def parse_input(file_name: str):
    with open(file_name, "r") as fp:
        rules, data = fp.read().split("\n\n")
    rule_dict = {}
    for rule in rules.split("\n"):
        rule_number, commands = rule.split(": ")
        if commands[0] == '"':
            commands = commands[1:-1]
        else:
            commands = [
                seq.split(" ") if " " in seq else [seq]
                for seq in (commands.split(" | ") if " | " in commands else [commands])
            ]
        rule_dict[rule_number] = commands
    data = data.split("\n")
    return rule_dict, data


def run_seq(rules, seq, message):
    if not seq:
        yield message
    else:
        k, *seq = seq
        for message in run(rules, k, message):
            yield from run_seq(rules, seq, message)


def run_list(rules, list_, message):
    for seq in list_:
        yield from run_seq(rules, seq, message)


def run(rules, k, message):
    if isinstance(rules[k], list):
        yield from run_list(rules, rules[k], message)
    if message and message[0] == rules[k]:
        yield message[1:]


def match_string(rules, message):
    return any([s == "" for s in run(rules, "0", message)])


if __name__ == "__main__":
    rules, data = parse_input("input.txt")
    print(sum([match_string(rules, s) for s in data]))
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]
    print(sum([match_string(rules, s) for s in data]))
