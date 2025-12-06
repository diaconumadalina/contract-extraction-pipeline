import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "src" / "pipeline" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)  # ensures folder exists

LOG_FILE = LOG_DIR / "app.log"


def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
