"""Pytest configuration: non-interactive Matplotlib before any test imports."""

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
