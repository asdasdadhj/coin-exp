import { NextResponse } from 'next/server';
import { fetchCryptoPrices } from '@/lib/crypto';

export async function GET() {
  try {
    const prices = await fetchCryptoPrices();
    
    return NextResponse.json(prices, {
      headers: {
        'Cache-Control': 'no-store, no-cache, must-revalidate, proxy-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
      },
    });
  } catch (error) {
    console.error('API Error:', error);
    
    return NextResponse.json(
      { 
        error: 'Failed to fetch cryptocurrency prices',
        message: error instanceof Error ? error.message : 'Unknown error'
      },
      { 
        status: 500,
        headers: {
          'Cache-Control': 'no-store',
        },
      }
    );
  }
}

export const dynamic = 'force-dynamic';
export const revalidate = 0;
