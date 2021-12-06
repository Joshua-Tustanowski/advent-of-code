import matplotlib.pyplot as plt
import seaborn as sns
from solutions_2021 import get_filename
from solutions_2021.day_5.solution import solution

sns.set()


def plot_results() -> None:
    file = get_filename()
    ocean_floor, _ = solution(file)
    plt.figure(figsize=(10, 10))
    sns.heatmap(ocean_floor.export(), cbar=None, xticklabels=False, yticklabels=False)
    plt.savefig("reddit.png", bbox_inches="tight", dpi=1000)


if __name__ == "__main__":
    plot_results()
