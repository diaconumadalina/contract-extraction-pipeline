from src.preprocess.regex_cleaner import apply_regex_cleaning
from src.preprocess.chunker import chunk_document
from src.preprocess.normalizer import normalize_text


def preprocess_text(raw_text: str) -> list[str]:
    """
    Full preprocessing pipeline:
    1. normalize unicode + whitespace
    2. apply regex cleaning
    3. chunk the text
    """
    text = normalize_text(raw_text)
    text = apply_regex_cleaning(text)
    chunks = chunk_document(text)

    return chunks
