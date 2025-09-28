# Cryptocurrency Price Tracker

A complete full-stack cryptocurrency price tracking application with both Python Flask backend and Next.js frontend implementations.

## Project Structure

coin-exp/
├── backend/           # Python Flask application
│   ├── crypto_tracker.py
│   ├── requirements.txt
│   ├── setup.sh
│   ├── venv/
│   └── README_CRYPTO.md
├── frontend/          # Next.js TypeScript application
│   ├── src/
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.ts
│   └── README.md
└── README.md         # This file

## Features

### Backend (Python Flask with uv)
- **Command-line interface** with beautiful terminal output
- **Web interface** with Bootstrap styling
- **JSON API** endpoint for price data
- **Real-time data** from Binance public API
- **Auto-refresh** functionality
- **Error handling** and retry logic
- **Modern Python packaging** with uv and pyproject.toml

### Frontend (Next.js)
- **Server-side rendering** for fast initial load
- **Client-side auto-refresh** every 30 seconds
- **Responsive design** with Tailwind CSS
- **TypeScript** for type safety
- **Modern UI** with gradient cards and animations
- **Mobile-first** responsive design

## Quick Start

### Backend (Python Flask)

```bash
cd backend
./setup.sh

# Command-line interface
source venv/bin/activate && python crypto_tracker.py

# Web interface
source venv/bin/activate && python crypto_tracker.py --web
```

### Frontend (Next.js)

```bash
cd frontend
yarn install
yarn dev
```

## Live Demos

- **Backend Web**: http://localhost:8080
- **Backend API**: http://localhost:8080/prices
- **Frontend**: http://localhost:3000
- **Frontend API**: http://localhost:3000/api/prices

## API Endpoints

Both implementations provide similar JSON API responses:

```json
{
  "BTC": 43210.50,
  "ETH": 2456.78,
  "timestamp": "2024-01-15T10:30:45.123456",
  "currency": "USDT"
}
```

## Technology Stack

### Backend
- **Python 3.9+**
- **uv** for fast package management
- **Flask** web framework
- **Requests** for API calls
- **Bootstrap 5** for styling
- **Font Awesome** icons

### Frontend
- **Next.js 13+** with App Router
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **React Hooks** for state management
- **Binance API** integration

## Features Comparison

| Feature | Backend (Flask) | Frontend (Next.js) |
|---------|----------------|-------------------|
| Command-line | | |
| Web interface | | |
| Auto-refresh | | |
| Mobile responsive | | |
| TypeScript | | |
| Server-side rendering | | |
| Modern animations | | |

## Development

### Prerequisites
- **Python 3.7+** (for backend)
- **Node.js 18+** (for frontend)
- **Internet connection** (for API access)

### Environment Setup

**Backend:**
```bash
cd backend
uv sync
```

**Frontend:**
```bash
cd frontend
yarn install
```

## Deployment

### Backend Deployment
- Can be deployed to any Python hosting service
- Supports Docker containerization
- Works with Heroku, Railway, DigitalOcean, etc.

### Frontend Deployment
- Optimized for Vercel deployment
- Supports Netlify, AWS Amplify
- Static export available for CDN hosting

## Documentation

- **Backend**: See `backend/README_CRYPTO.md`
- **Frontend**: See `frontend/README.md`

## Contributing

1. Fork the repository
2. Choose backend or frontend (or both!)
3. Create a feature branch
4. Make your changes
5. Submit a pull request

## License

This project is open source and available under the MIT License.
