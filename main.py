import pandas as pd
import aiohttp
import asyncio
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.keypair import Keypair
from nft_volume_analyzer import NFTVolumeAnalyzer
from nft_trading_executor import NFTTradingExecutor

async def main():
    analyzer = NFTVolumeAnalyzer()
    executor = NFTTradingExecutor()

    try:
        # Fetch and analyze collections
        collections_df = pd.DataFrame([{"symbol": "degods", "name": "DeGods", "total_items": 1000}])
        analyzed = analyzer.analyze_collections(collections_df)
        print(analyzed)

        # Fetch floor listings and execute a trade
        if not analyzed.empty:
            floor_listings = await executor.fetch_floor_listings(analyzed.iloc[0]['symbol'])
            if floor_listings:
                first_listing = floor_listings[0]
                await executor.execute_buy(first_listing['mintAddress'], first_listing['price'])
    finally:
        await executor.close()

if __name__ == "__main__":
    asyncio.run(main())
