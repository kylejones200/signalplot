# Changelog

All notable changes to this project are documented in this file. The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

Nothing yet.

## [0.1.3] — 2026-04-21

### Added

- Pytest suite under `tests/` (public API, `apply()` / `save()`, figures, `patch_pyplot` in a subprocess).
- Optional `dev` extra in `pyproject.toml` (`pytest`, `ruff`, `mypy`, `numpy` for examples and gallery regen).
- Ruff configuration (lint + enforced `ruff format` on `signalplot`, `tests`, `scripts`) and mypy configuration scoped to `signalplot/`.
- `CONTRIBUTING.md` with setup, checks, docs build, and gallery regeneration.
- `RELEASING.md` for maintainer release steps.
- GitHub issue templates (bug, feature, documentation, design proposal).
- Sphinx **Guides**: `defaults_and_save`, `axes_and_charts`, `labels_and_events`, `interop_and_stability`.
- `scripts/regen_gallery.py` to rebuild `docs/_static/gallery/` from `examples/`; docs CI runs it before HTML build.
- **Documentation** URL in `pyproject.toml` `[project.urls]` (GitHub Pages).
- README link to the hosted documentation site.
- Changelog entries for this release.

### Changed

- CI runs `ruff format --check`, `ruff check`, `mypy`, `pytest`, then builds distributions.
- Docs workflow runs the same Ruff and mypy steps after `pytest`, then regenerates gallery PNGs and builds HTML.
- `docs/conf.py` sets `release` from `signalplot.__version__`.
- `pre-push` hook installs `mypy`, runs format check, lint, mypy, pytest, build, and smoke save (with `trap` cleanup for `test_output.png`).
- `setup-hooks.sh` resolves the repo root, verifies `.githooks/`, and marks hooks executable.
- `style_scatter_plot` narrows Matplotlib collections to `PathCollection` before styling (runtime clarity; stubs need small `type: ignore` on plural setters).
- GitHub Actions workflows opt into **Node 24** for JavaScript actions (`FORCE_JAVASCRIPT_ACTIONS_TO_NODE24`).
