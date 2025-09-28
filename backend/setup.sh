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
echo "Development:"
echo "  uv add <package>                          # Add dependency"
echo "  uv run ruff format . && uv run ruff check .  # Format & lint"
echo "  ./ci.sh                                   # Run all CI checks"
