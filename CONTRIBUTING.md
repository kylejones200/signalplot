# Contributing to SignalPlot

Thank you for helping improve SignalPlot. The project stays intentionally small: disciplined Matplotlib defaults and a few helpers, not a second plotting stack.

## Principles

Before changing behavior or adding API surface, read the **Style Contract** and design notes in [README.md](README.md). New code should match existing naming, typing, and documentation style in `signalplot/`.

## Environment

Use Python 3.11 or newer (see `requires-python` in `pyproject.toml`). A virtual environment is strongly recommended:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev,docs]"
```

Install optional **git hooks** so pushes run the same checks as CI (Ruff format/lint, mypy, pytest, build, smoke save):

```bash
./setup-hooks.sh
```

Use `PYTHON=/path/to/python git push` if your default `python3` is not the venv you develop in. With **uv**, a typical flow is `uv venv && source .venv/bin/activate && uv pip install -e ".[dev,docs]"` then the same checks below.

## Checks to run locally

```bash
ruff format --check signalplot tests scripts   # or: ruff format signalplot tests scripts
ruff check signalplot tests scripts
python -m mypy
pytest
python -m build
```

The pre-push hook installs `build`, `pytest`, `ruff`, and `mypy` with pip (without upgrading pip) if needed, then runs format check, lint, mypy, pytest, package build, and a short Matplotlib `Agg` smoke test.

## Documentation

Build the Sphinx site locally:

```bash
pip install -e ".[docs]"
sphinx-build -b html docs docs/_build/html
```

Example scripts live in `examples/`. Regenerate the Sphinx gallery PNGs after changing an example or anything that affects figure output:

```bash
pip install -e ".[dev]"   # includes numpy for examples
python scripts/regen_gallery.py
```

Committed files under `docs/_static/gallery/` should match what that script produces so the docs site and offline builds stay aligned. The docs CI job runs the same script before `sphinx-build`.

## Releases (maintainers)

See [RELEASING.md](RELEASING.md). In short: bump version fields together, update the changelog, run checks and docs, tag `v*`, push.

## Questions and changes

Use [GitHub Issues](https://github.com/kylejones200/signalplot/issues) for bugs, documentation gaps, and small feature ideas. Larger direction is discussed in [ROADMAP.md](ROADMAP.md).
