import re


def remove_page_markers(text: str) -> str:
    """
    Removes common page numbering formats like:
    'Page 1 of 10', 'Page 3', '1/10'
    """
    patterns = [
        r"Page\s+\d+\s+of\s+\d+",
        r"Page\s+\d+",
        r"\b\d+/\d+\b",
    ]
    for pat in patterns:
        text = re.sub(pat, "", text, flags=re.IGNORECASE)
    return text


def remove_headers_footers(text: str) -> str:
    """
    Removes repetitive headers/footers by detecting lines repeated too often.
    """
    lines = text.split("\n")
    frequency = {}

    for line in lines:
        stripped = line.strip()
        if stripped:
            frequency[stripped] = frequency.get(stripped, 0) + 1

    # consider header/footer if appears on > 20% of pages
    threshold = 0.2 * len(lines)

    cleaned_lines = [
        line for line in lines
        if frequency.get(line.strip(), 0) < threshold
    ]

    return "\n".join(cleaned_lines)


def remove_extra_whitespace(text: str) -> str:
    """
    Compress repeated empty lines / spaces.
    """
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def apply_regex_cleaning(text: str) -> str:
    """
    Apply all regex-based cleaners in one pass.
    """
    text = remove_page_markers(text)
    text = remove_headers_footers(text)
    text = remove_extra_whitespace(text)
    return text
