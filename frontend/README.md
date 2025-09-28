# 🚀 Next.js Crypto Price Tracker

A modern, responsive cryptocurrency price tracker built with Next.js 13+ App Router, TypeScript, and Tailwind CSS. Displays real-time Bitcoin and Ethereum prices from the Binance public API.

## ✨ Features

- **Next.js 13+ App Router** with TypeScript
- **Server-Side Rendering** for initial price data
- **Client-Side Auto-Refresh** every 30 seconds
- **Responsive Design** with Tailwind CSS
- **Real-Time Data** from Binance public API
- **Beautiful UI** with gradient cards and animations
- **Error Handling** with retry functionality
- **Loading States** and shimmer effects
- **Mobile-First** responsive design

## 🛠️ Tech Stack

- **Framework**: Next.js 13+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **API**: Binance Public API
- **Deployment**: Vercel-ready

## 📁 Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── api/prices/route.ts     # API route for prices
│   │   ├── prices/page.tsx         # Main prices page
│   │   ├── layout.tsx              # Root layout
│   │   ├── page.tsx                # Home page
│   │   └── globals.css             # Global styles
│   ├── components/
│   │   └── CryptoPriceCard.tsx     # Price card component
│   ├── lib/
│   │   └── crypto.ts               # Crypto utility functions
│   └── types/
│       └── crypto.ts               # TypeScript types
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── postcss.config.js
└── next.config.js
```

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   yarn install
   ```

3. **Run the development server**:
   ```bash
   yarn dev
   ```

4. **Open your browser** and navigate to:
   - **Home**: http://localhost:3000
   - **Prices**: http://localhost:3000/prices
   - **API**: http://localhost:3000/api/prices

## 📊 API Endpoints

### GET /api/prices

Returns current cryptocurrency prices in JSON format:

```json
{
  "btc": {
    "symbol": "BTC",
    "name": "Bitcoin",
    "price": 43210.50,
    "formattedPrice": "$43,210.50",
    "icon": "₿",
    "color": "from-orange-400 to-orange-600"
  },
  "eth": {
    "symbol": "ETH",
    "name": "Ethereum", 
    "price": 2456.78,
    "formattedPrice": "$2,456.78",
    "icon": "Ξ",
    "color": "from-blue-400 to-purple-600"
  },
  "timestamp": "2024-01-15T10:30:45.123Z",
  "lastUpdated": "2024-01-15T10:30:45.123Z"
}
```

## 🎨 Features Breakdown

### Server-Side Rendering
- Initial prices are fetched server-side for fast loading
- SEO-friendly with proper meta tags
- No loading state on first visit

### Auto-Refresh
- Prices update automatically every 30 seconds
- Visual countdown timer shows next update
- Manual refresh button available

### Responsive Design
- Mobile-first approach with Tailwind CSS
- Beautiful gradient cards with hover effects
- Smooth animations and transitions

### Error Handling
- Network error detection and display
- Retry functionality for failed requests
- Graceful fallbacks for missing data

## 🔧 Configuration

### Environment Variables

No environment variables required - uses public Binance API endpoints.

### Customization

**Update refresh interval** in `src/app/prices/page.tsx`:
```typescript
// Change from 30 seconds to desired interval
const refreshInterval = setInterval(fetchPrices, 30000);
```

**Add more cryptocurrencies** in `src/lib/crypto.ts`:
```typescript
// Add new crypto symbols to fetch function
const [btcPrice, ethPrice, adaPrice] = await Promise.all([
  fetchCryptoPrice('BTCUSDT'),
  fetchCryptoPrice('ETHUSDT'),
  fetchCryptoPrice('ADAUSDT'), // New crypto
]);
```

## 🚀 Deployment

### Vercel (Recommended)

1. **Push to GitHub**
2. **Connect to Vercel**
3. **Deploy automatically**

### Other Platforms

```bash
# Build for production
yarn build

# Start production server
yarn start
```

## 📱 Mobile Support

- Fully responsive design
- Touch-friendly interface
- Optimized for all screen sizes
- Progressive Web App ready

## 🔒 Security

- No API keys required (public endpoints)
- Client-side data fetching with proper error handling
- No sensitive data exposure

## 🎯 Performance

- Server-side rendering for fast initial load
- Optimized images and fonts
- Minimal JavaScript bundle
- Efficient re-rendering with React hooks

## 🐛 Troubleshooting

**Prices not loading?**
- Check internet connection
- Verify Binance API is accessible
- Check browser console for errors

**Build errors?**
- Ensure Node.js 18+ is installed
- Clear node_modules and reinstall
- Check TypeScript configuration

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

Built with ❤️ using Next.js, TypeScript, and Tailwind CSS
