#!/bin/bash

echo "🚀 Setting up Cryptocurrency Price Tracker"
echo "=========================================="

# Setup Backend (Python Flask with uv)
echo ""
echo "📦 Setting up Backend (Python Flask with uv)..."
cd backend

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

echo "Installing Python dependencies with uv..."
uv sync

echo "✅ Backend setup complete!"

# Setup Frontend (Next.js)
echo ""
echo "📦 Setting up Frontend (Next.js)..."
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies with Yarn..."
    yarn install
fi

echo "✅ Frontend setup complete!"

# Return to root directory
cd ..

echo ""
echo "Setup Complete!"
echo "=================="
echo ""
echo "Backend (Python Flask with uv):"
echo "  Command-line: cd backend && uv run python crypto_tracker.py"
echo "  Web server:   cd backend && uv run python crypto_tracker.py --web"
echo "  URL:          http://localhost:8080"
echo ""
echo "Frontend (Next.js):"
echo "  Dev server:   cd frontend && yarn dev"
echo "  URL:          http://localhost:3000"
echo ""
echo "API Endpoints:"
echo "  Backend API:  http://localhost:8080/prices"
echo "  Frontend API: http://localhost:3000/api/prices"
echo ""
echo "Happy coding!"
