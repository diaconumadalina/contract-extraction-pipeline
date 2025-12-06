import re
import unicodedata
from typing import AnyStr


def normalize_unicode(text: AnyStr) -> str:
    """
    Normalize unicode characters to NFC form.
    Ensures consistent representation of accents and special characters.
    """
    if not isinstance(text, str):
        text = text.decode("utf-8", errors="ignore")
    return unicodedata.normalize("NFC", text)


def remove_control_characters(text: str) -> str:
    """
    Remove non-printable control characters that may break downstream processing.
    """
    return "".join(ch for ch in text if ch.isprintable() or ch in "\n\t\r")


def normalize_whitespace(text: str) -> str:
    """
    Collapse multiple spaces and newlines into a cleaner structure.
    """
    # Replace Windows-style newlines
    text = text.replace("\r\n", "\n")

    # Collapse 3+ newlines into max 2
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Replace multiple spaces with a single space (but keep newlines)
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Strip trailing spaces on each line
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines).strip()


def normalize_text(text: AnyStr) -> str:
    """
    Full normalization pipeline for contract text.
    """
    text = normalize_unicode(text)
    text = remove_control_characters(text)
    text = normalize_whitespace(text)
    return text
