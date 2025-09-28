#!/usr/bin/env python3
"""
Fetches live ETH and BTC prices in USDT from Binance API
Provides both command-line interface and web interface
"""

import json
import sys
from datetime import datetime
from decimal import Decimal, getcontext
from typing import Any, Optional, Union

import requests
from flask import Flask, Response, jsonify

# Set decimal precision for financial calculations
getcontext().prec = 28


class DecimalJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder that serializes Decimal as string to preserve precision"""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


app = Flask(__name__)

# Configure Flask to use custom JSON encoder for Decimal serialization
app.json_encoder = DecimalJSONEncoder  # type: ignore[attr-defined]


class CryptoPriceTracker:
    """Class to handle cryptocurrency price fetching from Binance API"""

    def __init__(self) -> None:
        self.base_url = "https://api.binance.com/api/v3/ticker/price"

    def get_price(self, symbol: str) -> Optional[Decimal]:
        """Fetch price for a specific trading pair"""
        try:
            url = f"{self.base_url}?symbol={symbol}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return Decimal(str(data["price"]))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Error parsing price data for {symbol}: {e}")
            return None

    def get_crypto_prices(self) -> dict[str, Union[Decimal, str, None]]:
        """Fetch both ETH and BTC prices in USDT"""
        eth_price = self.get_price("ETHUSDT")
        btc_price = self.get_price("BTCUSDT")

        return {
            "ETH": eth_price,
            "BTC": btc_price,
            "timestamp": datetime.now().isoformat(),
            "currency": "USDT",
        }


# Initialize price tracker
tracker = CryptoPriceTracker()


def display_prices_cli() -> None:
    """Command-line interface to display current prices"""
    print("=" * 50)
    print("🚀 CRYPTOCURRENCY PRICE TRACKER 🚀")
    print("=" * 50)

    prices = tracker.get_crypto_prices()

    eth_price = prices["ETH"]
    btc_price = prices["BTC"]
    timestamp = prices["timestamp"]

    if eth_price is not None and btc_price is not None and isinstance(timestamp, str):
        print(f"📈 Current Prices (as of {timestamp[:19]})")
        print("-" * 50)
        print(f"💎 Ethereum (ETH): ${eth_price:,.2f} USDT")
        print(f"₿  Bitcoin (BTC):  ${btc_price:,.2f} USDT")
        print("-" * 50)

        # Calculate market cap difference (approximate)
        if (
            isinstance(btc_price, Decimal)
            and isinstance(eth_price, Decimal)
            and btc_price > 0
            and eth_price > 0
        ):
            btc_eth_ratio = btc_price / eth_price
            print(f"📊 BTC/ETH Ratio: {btc_eth_ratio:.2f}")

        print("✅ Data fetched successfully from Binance API")
    else:
        print("❌ Failed to fetch cryptocurrency prices")

    print("=" * 50)


# Flask Routes
@app.route("/prices")
def get_prices_json() -> Union[Response, tuple[Response, int]]:
    """API endpoint that returns current prices as JSON"""
    prices = tracker.get_crypto_prices()

    if prices["ETH"] is None or prices["BTC"] is None:
        return jsonify(
            {"error": "Failed to fetch prices", "timestamp": datetime.now().isoformat()}
        ), 500

    # Return Decimal values directly - custom JSON encoder will serialize as strings
    return jsonify(prices)


@app.route("/")
def index() -> dict[str, Union[str, dict[str, str]]]:
    """API root endpoint with service information"""
    return {
        "service": "Cryptocurrency Price Tracker API",
        "version": "1.0.0",
        "endpoints": {"prices": "/prices", "health": "/health"},
        "description": "Backend API for fetching live cryptocurrency prices from Binance",
    }


@app.route("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "crypto-tracker-backend",
    }


def main() -> None:
    """Main function to handle command-line usage"""
    if len(sys.argv) > 1:
        if sys.argv[1] == "--api":
            print("🌐 Starting API server...")
            print("🔗 API endpoints:")
            print("   - http://localhost:8080/prices")
            print("   - http://localhost:8080/health")
            print("   - http://localhost:8080/ (service info)")
            print("⏹️  Press Ctrl+C to stop")
            app.run(debug=True, host="0.0.0.0", port=8080)
        elif sys.argv[1] == "--help":
            print("Cryptocurrency Price Tracker Backend API")
            print("Usage:")
            print("  python crypto_tracker.py           # Show prices in terminal")
            print("  python crypto_tracker.py --api     # Start API server")
            print("  python crypto_tracker.py --help    # Show this help")
        else:
            print("Unknown argument. Use --help for usage information.")
    else:
        display_prices_cli()


if __name__ == "__main__":
    main()
