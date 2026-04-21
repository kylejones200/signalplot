from __future__ import annotations

import signalplot as sp


def test_version_is_non_empty_string() -> None:
    assert isinstance(sp.__version__, str)
    assert sp.__version__.strip()


def test_public_api_surface() -> None:
    for name in sp.__all__:
        assert hasattr(sp, name), f"missing __all__ export: {name!r}"


def test_version_matches_pyproject() -> None:
    import re
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    text = (root / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE)
    assert match is not None
    assert match.group(1) == sp.__version__
