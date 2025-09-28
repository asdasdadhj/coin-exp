#!/bin/bash

echo "🚀 Setting up Cryptocurrency Price Tracker..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "📥 Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "✅ Setup complete!"
echo ""
echo "Usage:"
echo "  source venv/bin/activate && python crypto_tracker.py           # Command-line interface"
echo "  source venv/bin/activate && python crypto_tracker.py --web     # Web interface"
echo "  source venv/bin/activate && python crypto_tracker.py --help    # Show help"
