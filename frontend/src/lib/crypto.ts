import { BinancePrice, CryptoPrice, CryptoPricesData } from '@/types/crypto';

const BINANCE_API_BASE = 'https://api.binance.com/api/v3/ticker/price';

/**
 * Fetch price for a specific cryptocurrency symbol from Binance API
 */
async function fetchCryptoPrice(symbol: string): Promise<number> {
  try {
    const response = await fetch(`${BINANCE_API_BASE}?symbol=${symbol}`, {
      next: { revalidate: 0 }, // Always fetch fresh data
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch ${symbol}: ${response.statusText}`);
    }
    
    const data: BinancePrice = await response.json();
    return parseFloat(data.price);
  } catch (error) {
    console.error(`Error fetching ${symbol}:`, error);
    throw error;
  }
}

/**
 * Format price with proper currency formatting
 */
function formatPrice(price: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(price);
}

/**
 * Fetch both BTC and ETH prices from Binance API
 */
export async function fetchCryptoPrices(): Promise<CryptoPricesData> {
  try {
    // Fetch both prices concurrently
    const [btcPrice, ethPrice] = await Promise.all([
      fetchCryptoPrice('BTCUSDT'),
      fetchCryptoPrice('ETHUSDT'),
    ]);

    const timestamp = new Date().toISOString();

    return {
      btc: {
        symbol: 'BTC',
        name: 'Bitcoin',
        price: btcPrice,
        formattedPrice: formatPrice(btcPrice),
        icon: '₿',
        color: 'from-orange-400 to-orange-600',
      },
      eth: {
        symbol: 'ETH',
        name: 'Ethereum',
        price: ethPrice,
        formattedPrice: formatPrice(ethPrice),
        icon: 'Ξ',
        color: 'from-blue-400 to-purple-600',
      },
      timestamp,
      lastUpdated: new Date(),
    };
  } catch (error) {
    console.error('Error fetching crypto prices:', error);
    throw new Error('Failed to fetch cryptocurrency prices');
  }
}

/**
 * Client-side function to fetch prices (for auto-refresh)
 */
export async function fetchPricesClient(): Promise<CryptoPricesData> {
  try {
    const response = await fetch('/api/prices', {
      cache: 'no-store',
    });
    
    if (!response.ok) {
      throw new Error('Failed to fetch prices from API');
    }
    
    const data = await response.json();
    return {
      ...data,
      lastUpdated: new Date(data.timestamp),
    };
  } catch (error) {
    console.error('Error fetching prices from client:', error);
    throw error;
  }
}
