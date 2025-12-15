from __future__ import annotations

__version__ = "0.1.0"

from .axes import (
    add_range_frame,
    finish,
    force_bar_zero,
    style_bar_plot,
    style_line_plot,
    style_scatter_plot,
    tidy_axes,
)
from .labels import accent_point, direct_label, emphasize_last, event_line, note
from .style import ACCENT, SaveDefaults, apply, patch_pyplot, save, savefig

__all__ = [
    "__version__",
    "SaveDefaults",
    "ACCENT",
    "apply",
    "save",
    "savefig",
    "patch_pyplot",
    "add_range_frame",
    "tidy_axes",
    "finish",
    "style_line_plot",
    "style_scatter_plot",
    "style_bar_plot",
    "direct_label",
    "note",
    "emphasize_last",
    "accent_point",
    "event_line",
    "force_bar_zero",
]


