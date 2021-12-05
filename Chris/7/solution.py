import re
from functools import lru_cache


def read_and_parse_input_file_into_graph(file_name: str) -> dict:
    def parse_bag_content(content):
        num, *names = content.split(" ")
        return int(num), " ".join(names)

    with open(file_name, "r") as file:
        lines = file.readlines()

        # parse using regular expressions (thanks Josh)
        holding_bag_regex = re.compile(r"^(\w+\s\w+)")
        bag_content_regex = re.compile(r"(\d\s\w+\s\w+)")

        # Thought about default dict, but actually just dict comprehension of list comprehension seems to do the job
        return {
            holding_bag_regex.findall(line)[0]: [
                parse_bag_content(content) for content in bag_content_regex.findall(line)
            ]
            for line in lines
        }


def num_possible_containers(graph, target_colour):
    @lru_cache(256)
    def has_target_colour(colour: str, target_colour: str) -> bool:
        colour_contents = graph.get(colour)
        return any(
            inner_colour == target_colour or has_target_colour(inner_colour, target_colour)
            for num_colour, inner_colour in colour_contents
        )

    return sum(
        has_target_colour(outermost_colour, target_colour)
        for outermost_colour in graph
        if outermost_colour != target_colour
    )


def total_inner_bags(graph, start_colour):
    @lru_cache(256)
    def num_bags_contained(colour: str) -> 0:
        bag_contents = graph.get(colour)
        return sum(
            num_inner_bags * (1 + num_bags_contained(inner_colour)) for num_inner_bags, inner_colour in bag_contents
        )

    return num_bags_contained(start_colour)


if __name__ == "__main__":
    graph = read_and_parse_input_file_into_graph("rules.txt")
    # ------------ part 1 ------------
    print(num_possible_containers(graph, "shiny gold"))
    # ------------ part 2 ------------
    print(total_inner_bags(graph, "shiny gold"))
