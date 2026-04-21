#!/usr/bin/env bash
# Point this repository at hooks in .githooks/ (run from anywhere inside the repo).

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
    echo "Error: not inside a Git repository." >&2
    exit 1
}

cd "$ROOT"

if [ ! -d .githooks ]; then
    echo "Error: .githooks/ not found at repository root." >&2
    exit 1
fi

chmod +x .githooks/* 2>/dev/null || true

echo "Setting up git hooks in ${ROOT}..."

git config core.hooksPath .githooks

echo "✓ Git hooks configured (core.hooksPath=.githooks)"
echo "  Pre-push runs: ruff format + lint, mypy, pytest, build, and a short smoke save."
echo "  Override the interpreter with: PYTHON=/path/to/python git push"
