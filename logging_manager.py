import logging
from logging.handlers import RotatingFileHandler
from config import SolanaConfig

def setup_logging():
    """
    Configure comprehensive logging for the Solana NFT trading strategy.
    """
    logger = logging.getLogger("SolanaNFTTrading")
    logger.setLevel(getattr(logging, SolanaConfig.LOG_LEVEL))

    # File Handler
    file_handler = RotatingFileHandler(
        SolanaConfig.LOG_FILE, maxBytes=5_000_000, backupCount=5
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    # Stream Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger

# Global logger instance
logger = setup_logging()
