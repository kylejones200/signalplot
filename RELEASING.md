# Releasing SignalPlot

Short checklist for maintainers. Day-to-day contributing stays in [CONTRIBUTING.md](CONTRIBUTING.md).

## Before tagging

1. **Version** — Set the same value in `pyproject.toml` (`[project] version`) and `signalplot.__version__`. Tests assert they match.
2. **Changelog** — Add a dated section under [CHANGELOG.md](CHANGELOG.md) for this release (move items out of *Unreleased* when you cut the release).
3. **Quality** — `ruff format --check signalplot tests scripts`, `ruff check signalplot tests scripts`, `python -m mypy`, `pytest`, `python -m build`.
4. **Docs** — `sphinx-build -b html docs docs/_build/html`. If example plots changed, run `python scripts/regen_gallery.py` and commit updated files under `docs/_static/gallery/`.
5. **Main** — Merge to the default branch so CI is green.

## Tag and publish

Create an annotated tag matching `vMAJOR.MINOR.PATCH` and push it. CI builds distributions and publishes to PyPI when the ref matches `refs/tags/v*`.

## After release

Bump `__version__` / `pyproject.toml` to the next plausible version (e.g. patch +1 or new minor) and start a fresh *Unreleased* section in the changelog if you want to keep a running log.
