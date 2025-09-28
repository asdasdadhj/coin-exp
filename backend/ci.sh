#!/bin/bash

echo "🔍 Running CI Checks with uv (no venv needed)"
echo "=============================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Track overall status
OVERALL_STATUS=0

# Function to run a check and track status
run_check() {
    local name="$1"
    local command="$2"
    
    echo ""
    echo -e "${BLUE}📋 Running: $name${NC}"
    echo "----------------------------------------"
    
    if eval "$command"; then
        echo -e "${GREEN}✅ $name: PASSED${NC}"
    else
        echo -e "${RED}❌ $name: FAILED${NC}"
        OVERALL_STATUS=1
    fi
}

# Ensure we're in the right directory
cd "$(dirname "$0")"

# Check if uv is available
if ! command -v uv &> /dev/null; then
    echo -e "${RED}❌ uv is not installed. Please install uv first.${NC}"
    exit 1
fi

# 1. Ruff Linting (no project needed)
run_check "Ruff Linting" "uv tool run ruff check ."

# 2. Ruff Formatting Check (no project needed)
run_check "Ruff Format Check" "uv tool run ruff format --check ."

# 3. MyPy Type Checking (needs project dependencies)
run_check "MyPy Type Checking" "uv run --no-project --with mypy --with types-requests --with flask mypy crypto_tracker.py"

# 4. Application Smoke Test (needs project dependencies)
run_check "Application Smoke Test" "timeout 10s uv run python crypto_tracker.py --help"

echo ""
echo "=============================================="
if [ $OVERALL_STATUS -eq 0 ]; then
    echo -e "${GREEN}🎉 All CI checks PASSED! Ready for commit/deploy.${NC}"
else
    echo -e "${RED}💥 Some CI checks FAILED. Please fix the issues above.${NC}"
fi
echo "=============================================="

exit $OVERALL_STATUS
