"""Time series line plot example for SignalPlot."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    rng = np.random.default_rng(0)
    dates = np.arange(0, 24)
    values = np.cumsum(rng.normal(size=dates.size))

    plt.figure()
    plt.plot(dates, values, color="black", linewidth=1.5)
    plt.title("Monthly electricity demand")

    sp.save("time_series.png")
    plt.show()


if __name__ == "__main__":
    main()


