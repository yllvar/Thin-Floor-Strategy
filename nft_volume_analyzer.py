import requests
from solana.publickey import PublicKey
from solana.transaction import Transaction
from solana.rpc.async_api import AsyncClient
from solana.rpc.types import TxOpts
from solana.keypair import Keypair
from solders.pubkey import Pubkey
from solders.signature import Signature
from solders.transaction import Transaction as SoldersTransaction
from config import SolanaConfig, WALLET_CONFIG
from logging_manager import logger
import pandas as pd
import asyncio

class NFTVolumeAnalyzer:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {SolanaConfig.MAGIC_EDEN_API_KEY}"}

    def fetch_collection_stats(self, symbol: str) -> dict:
        """
        Fetch 7-day volume, floor price, and other stats for a given collection symbol.
        """
        url = f"{SolanaConfig.MAGIC_EDEN_API_BASE}/collections/{symbol}/stats"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            stats = response.json()
            logger.info(f"Stats for {symbol}: {stats}")
            return stats
        except requests.RequestException as e:
            logger.error(f"Error fetching stats for {symbol}: {e}")
            return {}

    def analyze_collections(self, collections: pd.DataFrame) -> pd.DataFrame:
        """
        Analyze collections to find those meeting volume and floor listing criteria.
        """
        filtered_collections = []

        for _, row in collections.iterrows():
            stats = self.fetch_collection_stats(row['symbol'])
            if not stats:
                continue

            # Check if stats meet criteria
            if (
                stats.get('seven_day_volume', 0) >= SolanaConfig.MIN_7DAY_VOLUME_THRESHOLD
                and stats.get('listed_count', 0) / row['total_items'] <= SolanaConfig.MAX_FLOOR_LISTINGS_PERCENTAGE
            ):
                filtered_collections.append({
                    "symbol": row['symbol'],
                    "name": row['name'],
                    "seven_day_volume": stats.get('seven_day_volume', 0),
                    "floor_price": stats.get('floor_price', 0) / 1e9  # Convert to SOL
                })

        logger.info(f"Filtered collections: {filtered_collections}")
        return pd.DataFrame(filtered_collections)
