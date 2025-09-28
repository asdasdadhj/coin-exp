#!/bin/bash

echo "🚀 Setting up Cryptocurrency Price Tracker"
echo "=========================================="

# Setup Backend (Python Flask)
echo ""
echo "📦 Setting up Backend (Python Flask)..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt
deactivate

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
echo "🎉 Setup Complete!"
echo "=================="
echo ""
echo "Backend (Python Flask):"
echo "  Command-line: cd backend && source venv/bin/activate && python crypto_tracker.py"
echo "  Web server:   cd backend && source venv/bin/activate && python crypto_tracker.py --web"
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
