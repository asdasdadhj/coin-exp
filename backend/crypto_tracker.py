#!/usr/bin/env python3
"""
Cryptocurrency Price Tracker
Fetches live ETH and BTC prices in USDT from Binance API
Provides both command-line interface and web interface
"""

import requests
import json
import sys
from flask import Flask, jsonify, render_template_string
from datetime import datetime

# Flask app setup
app = Flask(__name__)

class CryptoPriceTracker:
    """Class to handle cryptocurrency price fetching from Binance API"""
    
    def __init__(self):
        self.base_url = "https://api.binance.com/api/v3/ticker/price"
        
    def get_price(self, symbol):
        """Fetch price for a specific trading pair"""
        try:
            url = f"{self.base_url}?symbol={symbol}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return float(data['price'])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Error parsing price data for {symbol}: {e}")
            return None
    
    def get_crypto_prices(self):
        """Fetch both ETH and BTC prices in USDT"""
        eth_price = self.get_price("ETHUSDT")
        btc_price = self.get_price("BTCUSDT")
        
        return {
            "ETH": eth_price,
            "BTC": btc_price,
            "timestamp": datetime.now().isoformat(),
            "currency": "USDT"
        }

# Initialize price tracker
tracker = CryptoPriceTracker()

def display_prices_cli():
    """Command-line interface to display current prices"""
    print("=" * 50)
    print("🚀 CRYPTOCURRENCY PRICE TRACKER 🚀")
    print("=" * 50)
    
    prices = tracker.get_crypto_prices()
    
    if prices["ETH"] is not None and prices["BTC"] is not None:
        print(f"📈 Current Prices (as of {prices['timestamp'][:19]})")
        print("-" * 50)
        print(f"💎 Ethereum (ETH): ${prices['ETH']:,.2f} USDT")
        print(f"₿  Bitcoin (BTC):  ${prices['BTC']:,.2f} USDT")
        print("-" * 50)
        
        # Calculate market cap difference (approximate)
        if prices['BTC'] > 0 and prices['ETH'] > 0:
            btc_eth_ratio = prices['BTC'] / prices['ETH']
            print(f"📊 BTC/ETH Ratio: {btc_eth_ratio:.2f}")
        
        print("✅ Data fetched successfully from Binance API")
    else:
        print("❌ Failed to fetch cryptocurrency prices")
        print("Please check your internet connection and try again")
    
    print("=" * 50)

# Flask Routes
@app.route('/prices')
def get_prices_json():
    """API endpoint that returns current prices as JSON"""
    prices = tracker.get_crypto_prices()
    
    if prices["ETH"] is None or prices["BTC"] is None:
        return jsonify({
            "error": "Failed to fetch prices",
            "timestamp": datetime.now().isoformat()
        }), 500
    
    return jsonify(prices)

@app.route('/')
def index():
    """Main web interface with Bootstrap styling"""
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crypto Price Tracker</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .card {
                backdrop-filter: blur(10px);
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }
            .price-card {
                transition: transform 0.3s ease;
            }
            .price-card:hover {
                transform: translateY(-5px);
            }
            .crypto-icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            .price-value {
                font-size: 2.5rem;
                font-weight: bold;
                color: #28a745;
            }
            .loading {
                display: none;
            }
            .error {
                color: #dc3545;
            }
        </style>
    </head>
    <body>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-10">
                    <div class="card">
                        <div class="card-body text-center p-5">
                            <h1 class="text-white mb-4">
                                <i class="fas fa-chart-line"></i>
                                Cryptocurrency Price Tracker
                            </h1>
                            <p class="text-white-50 mb-5">Live prices from Binance API</p>
                            
                            <div id="loading" class="loading">
                                <div class="spinner-border text-light" role="status">
                                    <span class="visually-hidden">Loading...</span>
                                </div>
                                <p class="text-white mt-2">Fetching latest prices...</p>
                            </div>
                            
                            <div id="error" class="error d-none">
                                <i class="fas fa-exclamation-triangle"></i>
                                <p>Failed to fetch prices. Please try again.</p>
                            </div>
                            
                            <div id="prices" class="row">
                                <!-- Prices will be loaded here -->
                            </div>
                            
                            <div class="mt-4">
                                <button id="refreshBtn" class="btn btn-light btn-lg">
                                    <i class="fas fa-sync-alt"></i> Refresh Prices
                                </button>
                            </div>
                            
                            <div class="mt-4">
                                <small class="text-white-50">
                                    Last updated: <span id="timestamp">-</span>
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script>
            async function fetchPrices() {
                const loading = document.getElementById('loading');
                const error = document.getElementById('error');
                const pricesDiv = document.getElementById('prices');
                const timestampSpan = document.getElementById('timestamp');
                
                loading.style.display = 'block';
                error.classList.add('d-none');
                pricesDiv.innerHTML = '';
                
                try {
                    const response = await fetch('/prices');
                    const data = await response.json();
                    
                    if (response.ok) {
                        pricesDiv.innerHTML = `
                            <div class="col-md-6 mb-4">
                                <div class="card price-card h-100">
                                    <div class="card-body text-center">
                                        <div class="crypto-icon text-warning">
                                            <i class="fab fa-ethereum"></i>
                                        </div>
                                        <h3 class="text-white">Ethereum</h3>
                                        <div class="price-value">$${data.ETH.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
                                        <small class="text-white-50">ETH/USDT</small>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-6 mb-4">
                                <div class="card price-card h-100">
                                    <div class="card-body text-center">
                                        <div class="crypto-icon text-warning">
                                            <i class="fab fa-bitcoin"></i>
                                        </div>
                                        <h3 class="text-white">Bitcoin</h3>
                                        <div class="price-value">$${data.BTC.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</div>
                                        <small class="text-white-50">BTC/USDT</small>
                                    </div>
                                </div>
                            </div>
                        `;
                        
                        const timestamp = new Date(data.timestamp).toLocaleString();
                        timestampSpan.textContent = timestamp;
                    } else {
                        throw new Error('Failed to fetch prices');
                    }
                } catch (err) {
                    error.classList.remove('d-none');
                    console.error('Error fetching prices:', err);
                } finally {
                    loading.style.display = 'none';
                }
            }
            
            document.getElementById('refreshBtn').addEventListener('click', fetchPrices);
            
            // Load prices on page load
            fetchPrices();
            
            // Auto-refresh every 30 seconds
            setInterval(fetchPrices, 30000);
        </script>
    </body>
    </html>
    """
    
    return render_template_string(html_template)

def main():
    """Main function to handle command-line usage"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--web':
            print("🌐 Starting web server...")
            print("📱 Open http://localhost:8080 in your browser")
            print("🔗 API endpoint: http://localhost:8080/prices")
            print("⏹️  Press Ctrl+C to stop")
            app.run(debug=True, host='0.0.0.0', port=8080)
        elif sys.argv[1] == '--help':
            print("Cryptocurrency Price Tracker")
            print("Usage:")
            print("  python crypto_tracker.py           # Show prices in terminal")
            print("  python crypto_tracker.py --web     # Start web server")
            print("  python crypto_tracker.py --help    # Show this help")
        else:
            print("Unknown argument. Use --help for usage information.")
    else:
        display_prices_cli()

if __name__ == "__main__":
    main()
