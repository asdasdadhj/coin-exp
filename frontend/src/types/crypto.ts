export interface BinancePrice {
  symbol: string;
  price: string;
}

export interface CryptoPrice {
  symbol: string;
  name: string;
  price: number;
  formattedPrice: string;
  icon: string;
  color: string;
}

export interface CryptoPricesData {
  btc: CryptoPrice;
  eth: CryptoPrice;
  timestamp: string;
  lastUpdated: Date;
}
