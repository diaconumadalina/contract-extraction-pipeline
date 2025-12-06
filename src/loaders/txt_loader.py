from pathlib import Path

from src.preprocess.normalizer import normalize_text


def load_txt_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Load and normalize text from a plain .txt file.

    Args:
        path: Path to the .txt file.
        encoding: Text encoding, default utf-8.

    Returns:
        Normalized text content.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Text file not found: {path}")

    with path.open("r", encoding=encoding, errors="ignore") as f:
        raw_text = f.read()

    return normalize_text(raw_text)
