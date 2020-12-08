import re
from typing import List


def read_and_parse_input_file(file_name: str) -> str:
    with open(file_name, 'r') as file:
        contents = file.read()
        contents = contents.split("\n")

    # parse using regular expressions
    holding_bag_regex = re.compile(r'^(\w+\s\w+)')
    bag_content_regex = re.compile(r'(\d\s\w+\s\w+)')
    bag_names, bag_contents  = [], []
    for data in contents:
        bag_names.append(holding_bag_regex.match(data).group(0))
        bag_contents.append(bag_content_regex.findall(data))
    return bag_names, bag_contents


def build_graph(bag_names: List[str], bag_contents: List[str]) -> dict:
    graph = {}
    for i in range(len(bag_names)):
        bag = bag_names[i]
        graph[bag] = []
        for content in bag_contents[i]:
            if len(content):
                number, first, last = content.split(" ")
                content = (int(number), f'{first} {last}')
            else:
                content = []
            graph[bag].append(content)
    return graph


def traverse_graph(
    graph: dict,
    start_colour: str,
    target_colour: str,
    visited: list,
    queue: list,
    counter: bool = False,
    count: int = 0,
) -> bool:
    visited.append(start_colour)
    queue.append((0, start_colour))
    while queue:
        count, node = queue.pop(0)
        print(node, end=" ")
        if node == target_colour:
            print(f"Found target colour! {target_colour}")
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    if counter:
        return count
    return False


def search_all_start_nodes(graph, target_colour, count):
    for start_colour in graph.keys():
        queue, visited = [], []
        print(f"Bag colour: {start_colour}", end="\n")
        if len(graph[start_colour]) and start_colour != target_colour and traverse_graph(
            graph, start_colour, target_colour, visited, queue):
            count += 1
        print("\n")
    return count


def dfs(graph, stack, counter = 0):
    while len(stack):
        amount, colour = stack.pop()
        counter += amount

        if colour in graph:
            children = graph[colour]
            for number, child in children:
                stack.append((number*amount, child))
    return counter - 1


if __name__ == "__main__":
    bag_names, bag_contents = read_and_parse_input_file('input.txt')
    graph = build_graph(bag_names, bag_contents)
    # ------------ part 1 ------------
    # print(search_all_start_nodes(graph, target_colour='shiny gold', count=0))

    # ------------ part 2 ------------
    stack = [(1, "shiny gold")]
    # print(dfs(graph, stack))
