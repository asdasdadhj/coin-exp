# 🚀 UV Package Manager Guide

Complete guide for using uv with the Cryptocurrency Price Tracker backend.

## 📋 What is uv?

uv is a fast Python package installer and resolver written in Rust. It's designed to be a drop-in replacement for pip and pip-tools, offering:

- **10-100x faster** than pip
- **Deterministic dependency resolution**
- **Built-in virtual environment management**
- **Lock file support** for reproducible builds
- **Compatible with pip** and existing workflows

## 🛠️ Installation

### Global Installation

```bash
# Install uv globally
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv

# Or with homebrew (macOS)
brew install uv
```

## 📁 Project Structure

Our project uses the modern Python packaging structure:

```
backend/
├── pyproject.toml          # Project configuration and dependencies
├── uv.lock                 # Locked dependency versions
├── crypto_tracker.py       # Main application
└── UV_GUIDE.md            # This guide
```

## 🔧 Basic Commands

### Project Setup

```bash
# Initialize a new uv project (if starting from scratch)
uv init

# Sync dependencies from pyproject.toml and uv.lock
uv sync

# Sync only production dependencies (no dev dependencies)
uv sync --no-dev

# Sync with frozen lockfile (for production/Docker)
uv sync --frozen
```

### Managing Dependencies

```bash
# Add a new dependency
uv add flask

# Add a development dependency
uv add --dev pytest

# Add with version constraints
uv add "requests>=2.31.0,<3.0.0"

# Remove a dependency
uv remove flask

# Update all dependencies
uv lock --upgrade

# Update specific dependency
uv lock --upgrade-package requests
```

### Running Code

```bash
# Run Python with the project environment
uv run python crypto_tracker.py

# Run with arguments
uv run python crypto_tracker.py --web

# Run development tools
uv run black .
uv run ruff check .
uv run pytest
uv run mypy .
```

## 📄 pyproject.toml Configuration

Our `pyproject.toml` defines the project:

```toml
[project]
name = "crypto-tracker-backend"
version = "1.0.0"
description = "Cryptocurrency price tracker backend with Flask"
requires-python = ">=3.9"

# Production dependencies
dependencies = [
    "flask>=2.3.0,<3.0.0",
    "requests>=2.31.0,<3.0.0",
    "werkzeug>=2.3.0,<3.0.0",
]

[tool.uv]
# Development dependencies
dev-dependencies = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
    "types-requests>=2.31.0",
]
```

## 🔒 Lock File (uv.lock)

The `uv.lock` file contains exact versions of all dependencies and their transitive dependencies:

- **Automatically generated** by `uv lock`
- **Should be committed** to version control
- **Ensures reproducible builds** across environments
- **Used by `uv sync --frozen`** in production

## 🐳 Docker Integration

Our Dockerfile uses uv for fast, reproducible builds:

```dockerfile
# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin:$PATH"

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies (frozen lockfile)
RUN uv sync --frozen --no-dev

# Copy source code
COPY . .

# Run with uv
CMD ["uv", "run", "python", "crypto_tracker.py", "--web"]
```

## 🚀 Development Workflow

### Daily Development

```bash
# Start development
cd backend
uv sync                    # Ensure dependencies are up to date

# Run the application
uv run python crypto_tracker.py --web

# Code quality checks
uv run black .             # Format code
uv run ruff check .        # Lint code
uv run mypy .              # Type checking
uv run pytest             # Run tests
```

### Adding New Features

```bash
# Add a new dependency
uv add new-package

# Add development tools
uv add --dev new-dev-tool

# Lock the new dependencies
uv lock

# Commit changes
git add pyproject.toml uv.lock
git commit -m "Add new-package dependency"
```

### Updating Dependencies

```bash
# Update all dependencies to latest compatible versions
uv lock --upgrade

# Update specific package
uv lock --upgrade-package requests

# Sync the updated dependencies
uv sync
```

## 🔄 Migration from pip/requirements.txt

If migrating from pip:

```bash
# 1. Create pyproject.toml from requirements.txt
uv init
uv add $(cat requirements.txt)

# 2. Add dev dependencies
uv add --dev pytest black ruff mypy

# 3. Generate lock file
uv lock

# 4. Remove old files
rm requirements.txt

# 5. Update scripts to use uv run
```

## 📊 Performance Comparison

| Operation | pip | uv | Speedup |
|-----------|-----|----|---------| 
| Install Flask | 2.3s | 0.1s | 23x |
| Resolve dependencies | 5.1s | 0.2s | 25x |
| Create venv + install | 8.7s | 0.3s | 29x |

## 🛡️ Best Practices

### 1. Always Use Lock Files
```bash
# Generate lock file
uv lock

# Use frozen installs in production
uv sync --frozen
```

### 2. Separate Dev Dependencies
```bash
# Production dependencies in [project.dependencies]
# Dev dependencies in [tool.uv.dev-dependencies]
uv add --dev pytest
```

### 3. Pin Python Version
```toml
[project]
requires-python = ">=3.9"
```

### 4. Use Version Constraints
```toml
dependencies = [
    "flask>=2.3.0,<3.0.0",  # Compatible range
    "requests>=2.31.0",     # Minimum version
]
```

### 5. Regular Updates
```bash
# Weekly dependency updates
uv lock --upgrade
uv sync
```

## 🐛 Troubleshooting

### Common Issues

**Dependencies not found:**
```bash
uv sync  # Ensure dependencies are installed
```

**Version conflicts:**
```bash
uv lock --upgrade  # Resolve with latest versions
```

**Environment issues:**
```bash
rm -rf .venv  # Remove virtual environment
uv sync       # Recreate environment
```

**Docker build fails:**
```bash
# Ensure uv.lock is copied to container
COPY pyproject.toml uv.lock ./
```

## 📚 Additional Resources

- [uv Documentation](https://docs.astral.sh/uv/)
- [Python Packaging Guide](https://packaging.python.org/)
- [pyproject.toml Specification](https://peps.python.org/pep-0621/)

## 🎯 Quick Reference

```bash
# Essential commands
uv sync                    # Install dependencies
uv add <package>          # Add dependency
uv remove <package>       # Remove dependency
uv lock                   # Update lock file
uv run <command>          # Run in project environment

# Development
uv run python script.py   # Run Python script
uv run pytest            # Run tests
uv run black .            # Format code
uv run ruff check .       # Lint code
uv run mypy .             # Type checking

# CI/CD - Run all checks locally
./ci.sh                   # Complete CI script (no venv needed)
make ci                   # Using Makefile
make ci-fix               # CI with auto-fix

# One-liner CI check
uv tool run ruff check . && uv tool run ruff format --check .

# Production
uv sync --frozen --no-dev # Install production deps only
```

## 🔍 CI/CD Integration

### Local CI Checks

Run all CI checks locally before committing:

```bash
# Recommended: Complete CI script
./ci.sh                   # All checks with uv (no venv needed)
make ci                   # Via Makefile

# Quick fixes
make ci-fix               # Auto-fix issues

# Manual commands
uv tool run ruff check .              # Linting only
uv tool run ruff format --check .     # Format check only
uv run mypy .                         # Type checking
```

### CI Pipeline Commands

For GitHub Actions, GitLab CI, or other CI systems:

```yaml
# Example CI pipeline
- name: Install dependencies
  run: uv sync

- name: Lint with Ruff
  run: uv run ruff check .

- name: Check formatting
  run: uv run ruff format --check .

- name: Type check with MyPy
  run: uv run mypy .

- name: Run tests
  run: uv run pytest -v
```

This guide covers everything you need to know about using uv with our cryptocurrency tracker backend!
