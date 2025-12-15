"""Scatter-plot relationship example for SignalPlot."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    rng = np.random.default_rng(2)
    x = rng.normal(0, 1, 250)
    y = 0.6 * x + rng.normal(0, 0.7, 250)

    plt.figure()
    plt.scatter(x, y, s=20, color="black")
    plt.title("Load versus temperature")

    sp.save("scatter.png")
    plt.show()


if __name__ == "__main__":
    main()


