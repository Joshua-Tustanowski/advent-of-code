import re
from typing import Dict, List, Tuple


class Graph:
    def __init__(self):
        self.vertices = {}
        self.weights: Dict[Tuple[str, str], int] = {}

    def add_vertex(self, vertex_name: str):
        if vertex_name not in self.vertices:
            new_vertex = Vertex(vertex_name)
            self.vertices[vertex_name] = new_vertex

    def add_edge(self, from_: str, to: str):
        if from_ not in self.vertices:
            self.add_vertex(from_)

        if to not in self.vertices:
            self.add_vertex(to)
        self.vertices[from_].add_neighbour(self.vertices[to])

    def no_of_vertices_leading_to(self, to: str) -> int:
        total = 0
        for vertex_name in self.vertices.keys():
            if vertex_name == to:
                continue

    # def find_path(self, start, end, path=None):
    #     if path is None:
    #         path = []
    #     path = path + [start]
    #     if start == end:
    #         return path
    #     if start not in self.vertices:
    #         return None
    #     for node in self.vertices[start].adjacent:
    #         if node not in path:
    #             newpath = self.find_path(node, end, path)
    #             if newpath:
    #                 return newpath
    #     return None

    def find_all_paths(self, start: str, end: str, path=None) -> list:
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.vertices:
            return []

        paths = []
        for node in self.vertices[start].adjacent:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def populate_graph_with_input(self, inp: List[str]):
        for line in inp:
            components = line.split(" bags contain ")
            colour = components[0]
            if "no other bags" in line:
                self.add_vertex(colour)
            else:
                children_list = components[1]
                children = [c.split(" bag")[0] for c in children_list.split(",")]
                for child_str in children:
                    child_colour_wgt, child_colour = re.search(r"(\d)\s([\w\s]+)", child_str).groups()
                    self.add_edge(colour, child_colour)
                    self.weights[(colour, child_colour)] = int(child_colour_wgt)

    def find_no_of_parents(self, vertex: str):
        """Part 1"""
        colours_encountered = set()
        for v_name, v in self.vertices.items():
            if v_name == vertex:
                continue

            paths_between = self.find_all_paths(v_name, vertex)
            if paths_between:
                colours_encountered |= set.union(*[set(l) for l in paths_between])

        return len(colours_encountered) - 1

    def find_number_of_bags_inside(self, colour: str) -> int:
        """Part 2"""
        paths_from_colour = []
        for vertex_name, vertex in self.vertices.items():
            if vertex_name == colour:
                continue
            paths = self.find_all_paths(colour, vertex_name)
            if paths:
                paths_from_colour.extend(paths)

        # Count
        no_of_bags = 0
        for path in paths_from_colour:
            product = 1
            for i in range(len(path) - 1):
                pair = tuple(path[i : i + 2])
                product *= self.weights[pair]
            no_of_bags += product
        return no_of_bags


class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.adjacent = {}

    def add_neighbour(self, other_vertex):
        self.adjacent[other_vertex.name] = other_vertex


def part1(inp: List[str]) -> int:
    graph = Graph()
    graph.populate_graph_with_input(inp)
    return graph.find_no_of_parents("shiny gold")


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    inp1 = load_input_file("sample.txt")
    assert part1(inp1) == 4

    inp = load_input_file("input.txt")
    assert part1(inp) == 287


def part2(inp: List[str], top_colour: str) -> int:
    graph = Graph()
    graph.populate_graph_with_input(inp)
    return graph.find_number_of_bags_inside(top_colour)


def test_part2():
    inp1 = load_input_file("sample.txt")
    assert part2(inp1, "shiny gold") == 32

    inp = load_input_file("input.txt")
    assert part2(inp, "shiny gold") == 48160
