#!/bin/bash
# Setup script to install git hooks

echo "Setting up git hooks..."

# Configure git to use .githooks directory
git config core.hooksPath .githooks

if [ $? -eq 0 ]; then
    echo "✓ Git hooks configured successfully"
    echo "  Hooks will be loaded from .githooks/"
else
    echo "✗ Failed to configure git hooks"
    exit 1
fi
