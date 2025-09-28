# 🐳 Docker Deployment Guide

Complete containerization setup for the Cryptocurrency Price Tracker with separate containers for Flask backend and Next.js frontend using Docker Compose.

## 📋 Container Architecture

- **Backend Container**: Python 3.11-slim with Flask on port 8080
- **Frontend Container**: Node.js 18-alpine with Next.js on port 3000
- **Package Manager**: Yarn for frontend dependencies
- **Orchestration**: Docker Compose with custom network
- **Security**: Non-root users in both containers

## 🚀 Quick Start

### Using Docker Compose (Recommended)

```bash
# Build and run the container
docker-compose up --build

# Run in detached mode
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop the container
docker-compose down
```

### Using Docker Commands

```bash
# Build individual services
docker build -t crypto-backend ./backend
docker build -t crypto-frontend ./frontend

# Run backend container
docker run -d -p 8080:8080 --name crypto-backend crypto-backend

# Run frontend container
docker run -d -p 3000:3000 --name crypto-frontend crypto-frontend

# View logs
docker logs -f crypto-backend
docker logs -f crypto-frontend

# Stop containers
docker stop crypto-backend crypto-frontend
docker rm crypto-backend crypto-frontend
```

## 🌐 Access Points

Once the container is running:

- **Next.js Frontend**: http://localhost:3000
- **Flask Backend Web**: http://localhost:8080
- **Flask API**: http://localhost:8080/prices
- **Next.js API**: http://localhost:3000/api/prices

## 📁 Container Structure

**Backend Container (`crypto-backend`):**
```
/app/
├── crypto_tracker.py
├── requirements.txt
└── ... (other backend files)
```

**Frontend Container (`crypto-frontend`):**
```
/app/
├── src/
├── package.json
├── yarn.lock
├── .next/          # Built Next.js app
└── ... (other frontend files)
```

## 🔧 Configuration Files

### Backend Dockerfile Features

- **Base Image**: Python 3.11-slim for minimal footprint
- **Security**: Non-root user for running the application
- **Health Checks**: Built-in health monitoring
- **Dependency Caching**: Requirements installed separately for better layer caching
- **Port Exposure**: Port 8080 exposed

### Frontend Dockerfile Features

- **Base Image**: Node.js 18-alpine for minimal footprint
- **Package Manager**: Yarn with frozen lockfile for reproducible builds
- **Security**: Non-root user (nextjs) for running the application
- **Production Build**: Next.js optimized build during image creation
- **Health Checks**: Built-in health monitoring with wget
- **Port Exposure**: Port 3000 exposed

### Docker Compose Configuration

- **Multi-Container**: Separate containers for backend and frontend
- **Custom Network**: Isolated network for service communication
- **Health Checks**: Individual health monitoring for each service
- **Dependencies**: Frontend depends on backend startup
- **Auto-restart**: Both services restart automatically on failure

## 📊 Monitoring

### View Service Status

```bash
# Check all services status
docker-compose ps

# Enter backend container
docker-compose exec backend bash

# Enter frontend container  
docker-compose exec frontend sh

# View logs for specific service
docker-compose logs -f backend
docker-compose logs -f frontend

# View logs for all services
docker-compose logs -f

# Restart a specific service
docker-compose restart backend
docker-compose restart frontend
```

### Service Management

```bash
# Scale services (if needed)
docker-compose up --scale backend=2 --scale frontend=1

# Stop specific service
docker-compose stop backend
docker-compose stop frontend

# Remove and recreate services
docker-compose down
docker-compose up --build
```

## 🔍 Health Checks

The docker-compose configuration includes health checks:

```bash
# Check container health
docker-compose ps

# View health check logs for specific service
docker inspect coin-exp_backend_1 | grep -A 10 Health
docker inspect coin-exp_frontend_1 | grep -A 10 Health

# Test health endpoints directly
curl http://localhost:8080/prices  # Backend health
curl http://localhost:3000         # Frontend health
```

## 🛠️ Development

### Building for Development

```bash
# Build with no cache
docker-compose build --no-cache

# Build specific service
docker-compose build crypto-tracker
```

### Debugging

```bash
# Run container with shell access
docker run -it --entrypoint /bin/bash crypto-tracker

# Execute commands in running container
docker exec -it crypto-tracker /bin/bash

# View real-time logs
docker-compose logs -f crypto-tracker
```

## 🚀 Production Deployment

### Environment Variables

```bash
# Set production environment
export NODE_ENV=production
export FLASK_ENV=production

# Run with environment variables
docker run -e NODE_ENV=production -e FLASK_ENV=production \
  -p 3000:3000 -p 8080:8080 crypto-tracker
```

### Resource Limits

```yaml
# Add to docker-compose.yml
services:
  crypto-tracker:
    # ... existing config
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

## 🔒 Security Considerations

- **Non-root user**: Consider adding a non-root user for production
- **Secrets management**: Use Docker secrets for sensitive data
- **Network isolation**: Use custom networks for multi-container setups
- **Image scanning**: Scan images for vulnerabilities before deployment

## 📈 Performance Optimization

### Image Size Optimization

- Uses `.dockerignore` to exclude unnecessary files
- Multi-stage build potential for smaller production images
- Node.js production dependencies only

### Runtime Optimization

- Supervisord manages processes efficiently
- Next.js built for production (optimized bundles)
- Python dependencies cached in layers

## 🐛 Troubleshooting

### Common Issues

**Container won't start:**
```bash
# Check build logs
docker-compose build

# Check container logs
docker-compose logs crypto-tracker
```

**Services not accessible:**
```bash
# Verify port mapping
docker port crypto-tracker

# Check if services are running
docker exec crypto-tracker supervisorctl status
```

**Build failures:**
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

### Port Conflicts

If ports 3000 or 8080 are already in use:

```yaml
# Modify docker-compose.yml
ports:
  - "3001:3000"  # Use different host port
  - "8081:8080"  # Use different host port
```

## 📄 Files Overview

- **`Dockerfile`**: Multi-stage container definition
- **`supervisord.conf`**: Process management configuration
- **`docker-compose.yml`**: Container orchestration
- **`.dockerignore`**: Build optimization exclusions

This Docker setup provides a complete, production-ready containerized deployment of both the Flask backend and Next.js frontend applications.
