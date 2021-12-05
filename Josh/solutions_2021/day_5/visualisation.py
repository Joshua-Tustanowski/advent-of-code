import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from solutions_2021 import get_filename
from solutions_2021.day_5.solution import solution

sns.set()


def plot_results():
    file = get_filename()
    ocean_floor, _ = solution(file)
    plt.figure(figsize=(10, 10))
    ax = sns.heatmap(ocean_floor.export(), cbar=None, xticklabels=False, yticklabels=False)
    plt.savefig("vents.png", bbox_inches="tight", dpi=1000)


if __name__ == "__main__":
    plot_results()
