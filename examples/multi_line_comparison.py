"""Multiple line comparison example for SignalPlot."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    rng = np.random.default_rng(1)
    dates = np.arange(0, 24)
    region_a = np.cumsum(rng.normal(size=dates.size))
    region_b = np.cumsum(rng.normal(size=dates.size)) + 5

    plt.figure()
    plt.plot(dates, region_a, color="0.6", linewidth=1.0)
    plt.plot(dates, region_b, color="black", linewidth=1.5)
    plt.title("Regional demand comparison")

    sp.save("multi_line.png")
    plt.show()


if __name__ == "__main__":
    main()


