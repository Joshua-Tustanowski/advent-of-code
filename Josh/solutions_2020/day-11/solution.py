from typing import List, Tuple
import copy


def print_graph(graph):
    for i in range(len(graph)):
        print(graph[i])


def read_and_parse_input(file_name: str):
    with open(file_name, "r") as input_file:
        contents = input_file.readlines()
    for i, content in enumerate(contents):
        content = content.replace("\n", "")
        contents[i] = [char for char in content]
    return contents


def process_point(i: int, j: int, value: str, graph) -> str:
    count = 0
    adjacent = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
    if value == "L":
        tmp_cntr = 0
        for neighbour in adjacent:
            x_off, y_off = neighbour
            if 0 <= x_off + i < len(graph) and 0 <= y_off + j < len(graph[i]):
                if graph[x_off + i][y_off + j] != "#":
                    count += 1
            else:
                tmp_cntr += 1
        return count == len(adjacent) - tmp_cntr
    elif value == "#":
        for neighbour in adjacent:
            x_off, y_off = neighbour
            if 0 <= x_off + i < len(graph) and 0 <= y_off + j < len(graph[i]):
                if graph[x_off + i][y_off + j] == "#":
                    count += 1
        return count >= 4


def process_point_2(i: int, j: int, graph):
    directions = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
    tmp_cntr = 0
    hash_cntr = 0
    reg_cntr = 0
    for direction in directions:
        next_ = find_next_point(i, j, direction, graph)
        if next_ == -1:
            tmp_cntr += 1
        elif next_ == "#":
            hash_cntr += 1
        elif next_ != "#":
            reg_cntr += 1
    if graph[i][j] == "L":
        return reg_cntr == len(directions) - tmp_cntr
    if graph[i][j] == "#":
        return hash_cntr >= 5


def find_next_point(i: int, j: int, direction: Tuple[int, int], graph):
    x_off, y_off = i + direction[0], j + direction[1]
    while 0 <= x_off < len(graph) and 0 <= y_off < len(graph[i]):
        if graph[x_off][y_off] != ".":
            return graph[x_off][y_off]
        x_off += direction[0]
        y_off += direction[1]
    return -1


def fill_seats(graph: List[List[str]]) -> List[List[str]]:
    output = copy.deepcopy(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "L":
                count = process_point(i, j, graph[i][j], graph)
                output[i][j] = "#" if count else graph[i][j]
            elif graph[i][j] == "#":
                count = process_point(i, j, graph[i][j], graph)
                output[i][j] = "L" if count else graph[i][j]
            else:
                output[i][j] = graph[i][j]
    return output


def fill_seats_2(graph):
    output = copy.deepcopy(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "L":
                count = process_point_2(i, j, graph)
                output[i][j] = "#" if count else graph[i][j]
            elif graph[i][j] == "#":
                count = process_point_2(i, j, graph)
                output[i][j] = "L" if count else graph[i][j]
            else:
                output[i][j] = graph[i][j]
    return output


def same_graph(prev, graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != prev[i][j]:
                return False
    return True


def count_occupied(graph):
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == "#":
                count += 1
    return count


if __name__ == "__main__":
    graph = read_and_parse_input("input.txt")
    prev = graph
    while True:
        graph = fill_seats_2(graph)
        if same_graph(prev, graph):
            print(count_occupied(graph))
            break
        prev = graph
