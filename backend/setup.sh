#!/bin/bash

echo "🚀 Setting up Cryptocurrency Price Tracker with uv..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ uv is not installed. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# Sync dependencies with uv
echo "📥 Installing dependencies with uv..."
uv sync

echo "✅ Setup complete!"
echo ""
echo "Usage:"
echo "  uv run python crypto_tracker.py           # Command-line interface"
echo "  uv run python crypto_tracker.py --api     # API server"
echo "  uv run python crypto_tracker.py --help    # Show help"
echo ""
echo "Development commands:"
echo "  uv add <package>                          # Add new dependency"
echo "  uv add --dev <package>                    # Add dev dependency"
echo "  uv lock                                   # Update lock file"
echo "  uv sync                                   # Sync dependencies"
echo ""
echo "Code quality commands:"
echo "  uv run ruff check .                       # Lint code"
echo "  uv run ruff format .                      # Format code"
echo "  uv run black .                            # Alternative formatter"
echo "  uv run mypy .                             # Type checking"
echo "  uv run pytest                             # Run tests"
echo ""
echo "CI checks:"
echo "  ./ci-check.sh                             # Run all CI checks"
echo "  uv run ruff check . && uv run ruff format --check . && uv run mypy .  # Quick CI"
