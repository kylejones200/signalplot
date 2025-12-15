"""Event / regime highlight example for SignalPlot."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

import signalplot as sp


def main() -> None:
    sp.apply()

    rng = np.random.default_rng(4)
    dates = np.arange(0, 48)
    values = np.cumsum(rng.normal(size=dates.size))
    event_date = 24

    plt.figure()
    plt.plot(dates, values, color="black")
    plt.axvline(event_date, color="red", linewidth=1.0)
    plt.title("Demand with policy change")

    sp.save("event_line.png")
    plt.show()


if __name__ == "__main__":
    main()


