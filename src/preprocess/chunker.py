from langchain.text_splitter import RecursiveCharacterTextSplitter
import re
from typing import List


def split_by_headings(text: str) -> List[str]:
    """
    Try splitting by contract section headings such as:
    ARTICLE 1, SECTION 3, CHAPTER 2
    Returns multiple chunks if headings detected.
    """

    pattern = r"(ARTICLE\s+\d+|SECTION\s+\d+|CLAUSE\s+\d+|CHAPTER\s+\d+)"
    matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))

    if not matches:
        return []  # no headings → fallback

    chunks = []
    start_positions = [m.start() for m in matches] + [len(text)]

    for i in range(len(matches)):
        chunk = text[start_positions[i]:start_positions[i+1]].strip()
        chunks.append(chunk)

    return chunks


def split_by_length(text: str, chunk_size: int = 3000, overlap: int = 300) -> List[str]:
    """
    Default chunking using LangChain's RecursiveCharacterTextSplitter.
    Useful when no structural headings exist.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    return splitter.split_text(text)


def chunk_document(text: str) -> List[str]:
    """
    Hybrid chunking:
    1. Try structural split first
    2. If not applicable → fallback to token-length split
    """
    structural_chunks = split_by_headings(text)

    if structural_chunks:
        return structural_chunks

    return split_by_length(text)
