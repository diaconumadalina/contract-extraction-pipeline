from pathlib import Path

from src.loaders.pdf_loader import load_pdf_text
from src.loaders.txt_loader import load_txt_text


def load_document(path: str | Path) -> str:
    """
    Load a document by file extension and return normalized text.
    Supports PDF and TXT for now.
    """
    path = Path(path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return load_pdf_text(path)
    elif suffix in {".txt", ".log"}:
        return load_txt_text(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")
