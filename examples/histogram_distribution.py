"""Histogram distribution example for SignalPlot."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    rng = np.random.default_rng(3)
    values = rng.normal(size=1000)

    plt.figure()
    plt.hist(values, bins=30, color="0.7", edgecolor="black")
    plt.title("Distribution of daily demand")

    sp.save("histogram.png")
    plt.show()


if __name__ == "__main__":
    main()


