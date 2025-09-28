# Makefile for Crypto Tracker Backend
.PHONY: help install dev run test lint format type-check ci clean

# Default target
help:
	@echo "🚀 Crypto Tracker Backend - Available Commands"
	@echo "=============================================="
	@echo ""
	@echo "Setup:"
	@echo "  make install     Install dependencies"
	@echo "  make dev         Install with dev dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make run         Run CLI application"
	@echo "  make run-api     Run API server"
	@echo ""
	@echo "  make lint        Run ruff linting"
	@echo "  make format      Format code with ruff"
	@echo "  make type-check  Run mypy type checking"
	@echo ""
	@echo "CI/CD:"
	@echo "  make ci          Run all CI checks"
	@echo "  make ci-fix      Run CI checks with auto-fix"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean       Clean cache and temp files"

# Installation
	uv sync --no-dev

dev:
	uv sync

# Running
run:
	uv run python crypto_tracker.py

run-api:
	uv run python crypto_tracker.py --api

# Code quality
lint:
	uv run --no-project ruff check .

format:
	uv run --no-project ruff format .

type-check:
	uv run mypy .

test:
	uv run pytest -v

# CI checks
ci:
	./ci.sh

ci-fix:
	@uv run --no-project ruff check . --fix
	@uv run --no-project ruff format .
	@uv run mypy .

# Utilities
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
