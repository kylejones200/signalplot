from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import signalplot as sp


def test_apply_is_idempotent_for_core_rcparams() -> None:
    sp.apply()
    first = {
        k: mpl.rcParams[k]
        for k in (
            "figure.facecolor",
            "axes.facecolor",
            "axes.spines.top",
            "savefig.dpi",
            "font.family",
        )
    }
    sp.apply()
    second = {k: mpl.rcParams[k] for k in first}
    assert first == second


def test_save_writes_png(tmp_path: Path) -> None:
    sp.apply()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    out = tmp_path / "figure.png"
    sp.save(out)
    plt.close(fig)
    assert out.is_file()
    assert out.stat().st_size > 0


def test_savefig_alias_writes_file(tmp_path: Path) -> None:
    sp.apply()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    out = tmp_path / "via_alias.png"
    sp.savefig(out)
    plt.close(fig)
    assert out.is_file()


def test_save_accepts_overrides(tmp_path: Path) -> None:
    sp.apply()
    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])
    out = tmp_path / "hi.png"
    sp.save(out, dpi=72)
    plt.close(fig)
    assert out.is_file()
