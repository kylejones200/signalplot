from __future__ import annotations

import matplotlib.pyplot as plt
import signalplot as sp


def test_figure_returns_figure_and_axes() -> None:
    sp.apply()
    fig, ax = sp.figure()
    try:
        assert fig is not None
        ax.plot([0, 1], [0, 1])
    finally:
        plt.close(fig)


def test_small_multiples_returns_requested_axes_count() -> None:
    sp.apply()
    fig, axes = sp.small_multiples(4, ncols=2)
    try:
        assert len(axes) == 4
    finally:
        plt.close(fig)


def test_band_draws_without_error() -> None:
    sp.apply()
    fig, ax = plt.subplots()
    try:
        x = list(range(5))
        low = [i - 0.1 for i in x]
        high = [i + 0.1 for i in x]
        sp.band(ax, x, low, high)
        ax.plot(x, x, color="black")
    finally:
        plt.close(fig)
