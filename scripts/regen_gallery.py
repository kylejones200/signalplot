#!/usr/bin/env python3
"""Regenerate static gallery PNGs under docs/_static/gallery/.

Each example script is run with cwd set to the gallery directory so
``signalplot.save("*.png")`` writes the paths expected by docs/gallery.rst.

Requires numpy (used by the example scripts). From the repo root::

    pip install -e ".[dev]"
    python scripts/regen_gallery.py
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GALLERY = REPO / "docs" / "_static" / "gallery"

# Order matches docs/gallery.rst narrative.
EXAMPLE_SCRIPTS = [
    "examples/time_series_line.py",
    "examples/multi_line_comparison.py",
    "examples/scatter_relationship.py",
    "examples/histogram_distribution.py",
    "examples/bar_honest_scale.py",
    "examples/event_highlight.py",
]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    GALLERY.mkdir(parents=True, exist_ok=True)

    env = {
        **os.environ,
        "PYTHONPATH": str(REPO),
        "MPLBACKEND": "Agg",
        # Examples call plt.show(); Agg emits a harmless UserWarning.
        "PYTHONWARNINGS": "ignore:FigureCanvasAgg is non-interactive:UserWarning",
    }
    for rel in EXAMPLE_SCRIPTS:
        script = REPO / rel
        if not script.is_file():
            print(f"error: missing {rel}", file=sys.stderr)
            return 1
        print(f"running {rel} ...", flush=True)
        subprocess.run(
            [sys.executable, str(script)],
            cwd=GALLERY,
            env=env,
            check=True,
        )
    print(f"done: wrote PNGs under {GALLERY}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
