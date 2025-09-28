# 🚀 Cryptocurrency Price Tracker

A complete Python application that displays live Ethereum (ETH) and Bitcoin (BTC) prices in USDT using the Binance public API. Features both command-line interface and a beautiful web interface.

## ✨ Features

- **Live Price Fetching**: Real-time ETH and BTC prices from Binance API
- **Command-Line Interface**: Quick price display in terminal
- **Web Interface**: Beautiful Bootstrap-styled web app
- **JSON API**: RESTful endpoint for price data
- **Auto-refresh**: Web interface updates every 30 seconds
- **Error Handling**: Robust error handling for network issues
- **Responsive Design**: Mobile-friendly web interface

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Command-Line Interface

Display current prices in terminal:
```bash
python crypto_tracker.py
```

### Web Interface

Start the web server:
```bash
python crypto_tracker.py --web
```

Then open your browser and navigate to:
- **Main Interface**: http://localhost:5000
- **JSON API**: http://localhost:5000/prices

### Help

Show usage information:
```bash
python crypto_tracker.py --help
```

## 📊 API Endpoints

### GET /
Returns the main web interface with live price display.

### GET /prices
Returns JSON data with current cryptocurrency prices:

```json
{
  "ETH": 2456.78,
  "BTC": 43210.50,
  "timestamp": "2024-01-15T10:30:45.123456",
  "currency": "USDT"
}
```

## 🎨 Web Interface Features

- **Real-time Updates**: Prices refresh automatically every 30 seconds
- **Manual Refresh**: Click the refresh button for instant updates
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Beautiful UI**: Modern gradient background with glass-morphism cards
- **Loading States**: Visual feedback during data fetching
- **Error Handling**: User-friendly error messages

## 🔧 Technical Details

- **Data Source**: Binance Public API (no API key required)
- **Backend**: Python Flask framework
- **Frontend**: Bootstrap 5 + Font Awesome icons
- **HTTP Client**: Python requests library
- **Error Handling**: Comprehensive exception handling for network and parsing errors

## 📝 Example Output

### Command-Line:
```
==================================================
🚀 CRYPTOCURRENCY PRICE TRACKER 🚀
==================================================
📈 Current Prices (as of 2024-01-15T10:30:45)
--------------------------------------------------
💎 Ethereum (ETH): $2,456.78 USDT
₿  Bitcoin (BTC):  $43,210.50 USDT
--------------------------------------------------
📊 BTC/ETH Ratio: 17.58
✅ Data fetched successfully from Binance API
==================================================
```

## 🛡️ Error Handling

The application includes robust error handling for:
- Network connectivity issues
- API rate limiting
- Invalid API responses
- JSON parsing errors
- Server timeouts

## 🔄 Auto-refresh

The web interface automatically refreshes prices every 30 seconds. You can also manually refresh using the refresh button.

## 📱 Mobile Support

The web interface is fully responsive and works great on mobile devices with touch-friendly buttons and optimized layouts.

## 🚨 Requirements

- Python 3.7+
- Internet connection for API access
- Modern web browser (for web interface)

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## 📄 License

This project is open source and available under the MIT License.
