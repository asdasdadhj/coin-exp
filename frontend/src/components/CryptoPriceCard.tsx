'use client';

import { CryptoPrice } from '@/types/crypto';

interface CryptoPriceCardProps {
  crypto: CryptoPrice;
  isLoading?: boolean;
}

export default function CryptoPriceCard({ crypto, isLoading = false }: CryptoPriceCardProps) {
  return (
    <div className={`
      relative overflow-hidden rounded-2xl p-6 
      bg-gradient-to-br ${crypto.color} 
      shadow-2xl transform transition-all duration-300 
      hover:scale-105 hover:shadow-3xl
      ${isLoading ? 'animate-pulse' : ''}
    `}>
      {/* Background pattern */}
      <div className="absolute inset-0 bg-white/10 backdrop-blur-sm"></div>
      
      {/* Shimmer effect when loading */}
      {isLoading && (
        <div className="absolute inset-0 shimmer"></div>
      )}
      
      <div className="relative z-10">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-3">
            <div className="text-4xl font-bold text-white/90">
              {crypto.icon}
            </div>
            <div>
              <h3 className="text-xl font-bold text-white">
                {crypto.name}
              </h3>
              <p className="text-white/70 text-sm font-medium">
                {crypto.symbol}/USDT
              </p>
            </div>
          </div>
          
          {/* Status indicator */}
          <div className="flex items-center space-x-2">
            <div className="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <span className="text-white/70 text-xs font-medium">LIVE</span>
          </div>
        </div>
        
        {/* Price */}
        <div className="mb-4">
          {isLoading ? (
            <div className="h-10 bg-white/20 rounded-lg animate-pulse"></div>
          ) : (
            <div className="text-3xl font-bold text-white mb-1">
              {crypto.formattedPrice}
            </div>
          )}
          <p className="text-white/70 text-sm">
            Current Price
          </p>
        </div>
        
        {/* Additional info */}
        <div className="flex items-center justify-between text-sm">
          <span className="text-white/70">
            Market Cap Rank
          </span>
          <span className="text-white font-semibold">
            #{crypto.symbol === 'BTC' ? '1' : '2'}
          </span>
        </div>
        
        {/* Decorative elements */}
        <div className="absolute top-4 right-4 w-20 h-20 bg-white/5 rounded-full blur-xl"></div>
        <div className="absolute bottom-4 left-4 w-16 h-16 bg-white/5 rounded-full blur-lg"></div>
      </div>
    </div>
  );
}
