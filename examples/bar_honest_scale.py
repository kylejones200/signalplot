"""Bar chart with honest scale example for SignalPlot."""

from __future__ import annotations

import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    categories = ["Residential", "Commercial", "Industrial", "Other"]
    values = [120, 150, 90, 60]

    plt.figure()
    plt.bar(categories, values, color="0.6")
    plt.title("Average demand by sector")
    plt.ylim(bottom=0)

    sp.save("bar.png")
    plt.show()


if __name__ == "__main__":
    main()


