mult = lambda x, y: x * y
addr = lambda x, y: x + y


def part_two(data):
    def evaluate(stack):
        ans = 1
        op = mult
        while stack:
            ch = stack.pop()
            if ch == ")":
                return ans
            if ch == "(":
                ans = op(ans, evaluate(stack))
            elif ch == "+":
                op = addr
            elif ch == "*":
                ans = mult(ans, evaluate(stack))
                return ans
            else:
                ans = op(ans, int(ch))
        return ans

    ans = 0
    for line in data.split("\n"):
        stack = list(reversed(line.replace(" ", "")))
        ans += evaluate(stack)

    print(ans)


def part_one(data):
    def evaluate(stack):
        ans = 1
        op = mult
        while stack:
            ch = stack.pop()
            if ch == ")":
                return ans
            if ch == "(":
                ans = op(ans, evaluate(stack))
            elif ch == "+":
                op = addr
            elif ch == "*":
                op = mult
            else:
                ans = op(ans, int(ch))
        return ans

    ans = 0
    for line in data.split("\n"):
        stack = list(reversed(line.replace(" ", "")))
        ans += evaluate(stack)

    print(ans)


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        contents = fp.read()
    part_one(contents)
    part_two(contents)
