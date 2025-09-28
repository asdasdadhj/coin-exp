'use client';

import { useState, useEffect } from 'react';
import CryptoPriceCard from '@/components/CryptoPriceCard';
import { CryptoPricesData } from '@/types/crypto';
import { fetchPricesClient } from '@/lib/crypto';

export default function PricesPage() {
  const [pricesData, setPricesData] = useState<CryptoPricesData | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<Date | null>(null);
  const [countdown, setCountdown] = useState(30);

  // Fetch prices function
  const fetchPrices = async () => {
    try {
      setError(null);
      const data = await fetchPricesClient();
      setPricesData(data);
      setLastUpdated(new Date());
      setCountdown(30);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch prices');
    } finally {
      setIsLoading(false);
    }
  };

  // Initial fetch and auto-refresh setup
  useEffect(() => {
    fetchPrices();

    // Set up auto-refresh every 30 seconds
    const refreshInterval = setInterval(fetchPrices, 30000);

    // Countdown timer
    const countdownInterval = setInterval(() => {
      setCountdown((prev) => (prev > 0 ? prev - 1 : 30));
    }, 1000);

    return () => {
      clearInterval(refreshInterval);
      clearInterval(countdownInterval);
    };
  }, []);

  // Manual refresh handler
  const handleManualRefresh = () => {
    setIsLoading(true);
    fetchPrices();
  };

  return (
    <div className="min-h-screen p-4 md:p-8">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl md:text-6xl font-bold text-white mb-4">
            <span className="bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 bg-clip-text text-transparent">
              Crypto Prices
            </span>
          </h1>
          <p className="text-xl text-gray-300 mb-6">
            Real-time cryptocurrency prices from Binance API
          </p>
          
          {/* Status bar */}
          <div className="flex items-center justify-center space-x-6 text-sm text-gray-400">
            {lastUpdated && (
              <div className="flex items-center space-x-2">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                <span>
                  Last updated: {lastUpdated.toLocaleTimeString()}
                </span>
              </div>
            )}
            <div className="flex items-center space-x-2">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>Next update in {countdown}s</span>
            </div>
          </div>
        </div>

        {/* Error message */}
        {error && (
          <div className="mb-8 p-4 bg-red-500/20 border border-red-500/50 rounded-lg text-red-200 text-center">
            <p className="font-semibold">Error: {error}</p>
            <button 
              onClick={handleManualRefresh}
              className="mt-2 px-4 py-2 bg-red-500 hover:bg-red-600 rounded-lg text-white font-medium transition-colors"
            >
              Retry
            </button>
          </div>
        )}

        {/* Price cards */}
        <div className="grid md:grid-cols-2 gap-8 mb-8">
          {pricesData ? (
            <>
              <CryptoPriceCard crypto={pricesData.btc} isLoading={isLoading} />
              <CryptoPriceCard crypto={pricesData.eth} isLoading={isLoading} />
            </>
          ) : (
            <>
              <div className="h-64 bg-gray-800/50 rounded-2xl animate-pulse"></div>
              <div className="h-64 bg-gray-800/50 rounded-2xl animate-pulse"></div>
            </>
          )}
        </div>

        {/* Controls */}
        <div className="text-center">
          <button
            onClick={handleManualRefresh}
            disabled={isLoading}
            className={`
              px-8 py-3 rounded-xl font-semibold text-white transition-all duration-200
              ${isLoading 
                ? 'bg-gray-600 cursor-not-allowed' 
                : 'bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 hover:scale-105 shadow-lg hover:shadow-xl'
              }
            `}
          >
            {isLoading ? (
              <div className="flex items-center space-x-2">
                <svg className="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span>Refreshing...</span>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                </svg>
                <span>Refresh Now</span>
              </div>
            )}
          </button>
        </div>

        {/* Footer info */}
        <div className="mt-12 text-center text-gray-500 text-sm">
          <p>Data provided by Binance Public API</p>
          <p className="mt-1">Prices update automatically every 30 seconds</p>
        </div>
      </div>
    </div>
  );
}
