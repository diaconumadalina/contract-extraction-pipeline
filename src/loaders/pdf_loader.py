from pathlib import Path
from typing import Optional

import pdfplumber

from src.preprocess.normalizer import normalize_text


def load_pdf_text(
    pdf_path: str | Path,
    max_pages: Optional[int] = None,
    enable_ocr: bool = False,
) -> str:
    """
    Load text from a PDF file.
    For native PDFs, uses pdfplumber.
    For scanned PDFs, optional OCR can be enabled (placeholder implementation).

    Args:
        pdf_path: Path to the PDF file.
        max_pages: Optional maximum number of pages to read.
        enable_ocr: If True, attempt OCR for pages with no extractable text.

    Returns:
        Normalized text extracted from the PDF.
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    texts: list[str] = []

    with pdfplumber.open(pdf_path) as pdf:
        num_pages = len(pdf.pages)
        limit = min(num_pages, max_pages) if max_pages is not None else num_pages

        for i in range(limit):
            page = pdf.pages[i]
            page_text = page.extract_text() or ""

            if not page_text and enable_ocr:
                # Placeholder for OCR – can be implemented later with pytesseract + pdf2image
                # For now, we just skip the page or log a warning.
                # Example:
                # page_text = run_ocr_on_page(pdf_path, i)
                pass

            if page_text:
                texts.append(page_text)

    raw_text = "\n\n".join(texts)
    return normalize_text(raw_text)
