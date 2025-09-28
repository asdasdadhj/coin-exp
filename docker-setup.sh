#!/bin/bash

echo "🐳 Docker Setup for Cryptocurrency Price Tracker"
echo "================================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are available"
echo ""

# Build and start services
echo "🔨 Building Docker containers..."
docker-compose build

echo ""
echo "🚀 Starting services..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check service health
echo "🔍 Checking service health..."
echo ""

# Check backend
if curl -f http://localhost:8080/prices &> /dev/null; then
    echo "✅ Backend is healthy at http://localhost:8080"
else
    echo "⚠️  Backend might still be starting up..."
fi

# Check frontend
if curl -f http://localhost:3000 &> /dev/null; then
    echo "✅ Frontend is healthy at http://localhost:3000"
else
    echo "⚠️  Frontend might still be starting up..."
fi

echo ""
echo "🎉 Docker Setup Complete!"
echo "========================="
echo ""
echo "🌐 Access Points:"
echo "  Frontend:     http://localhost:3000"
echo "  Backend Web:  http://localhost:8080"
echo "  Backend API:  http://localhost:8080/prices"
echo "  Frontend API: http://localhost:3000/api/prices"
echo ""
echo "📊 Management Commands:"
echo "  View logs:    docker-compose logs -f"
echo "  Stop:         docker-compose down"
echo "  Restart:      docker-compose restart"
echo "  Rebuild:      docker-compose up --build"
echo ""
echo "Happy containerizing! 🐳"
