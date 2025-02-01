import os
from dataclasses import dataclass

@dataclass
class SolanaConfig:
    # Magic Eden API Configuration
    MAGIC_EDEN_API_KEY: str = os.getenv("MAGIC_EDEN_API_KEY", "")
    MAGIC_EDEN_API_BASE: str = "https://api-mainnet.magiceden.dev/v2"

    # Solana RPC Configuration
    SOLANA_RPC_ENDPOINT: str = os.getenv("SOLANA_RPC_ENDPOINT", "https://api.mainnet-beta.solana.com")

    # Strategy Parameters
    MIN_7DAY_VOLUME_THRESHOLD: int = 50_000  # USD
    MAX_FLOOR_LISTINGS_PERCENTAGE: float = 0.05  # 5% of collection
    MIN_COLLECTION_ITEMS: int = 100  # Minimum collection size

    # Trading Constraints
    MAX_PURCHASE_PRICE: float = 10.0  # SOL
    MAX_DAILY_TRADES: int = 5

    # Risk Management
    PORTFOLIO_ALLOCATION_PERCENTAGE: float = 0.1  # 10% of portfolio

    # Logging Configuration
    LOG_FILE: str = "solana_nft_trading.log"
    LOG_LEVEL: str = "INFO"


WALLET_CONFIG = {
    "private_key": os.getenv("WALLET_PRIVATE_KEY", ""),
    "public_key": os.getenv("WALLET_PUBLIC_KEY", ""),
}
