# chunker.py
from PyPDF2 import PdfReader
from typing import List

def read_pdf(file_path: str) -> List[str]:
    reader = PdfReader(file_path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return pages

def chunk_pages(pages: List[str], chunk_size: int = 500) -> List[str]:
    chunks = []
    for page in pages:
        words = page.split()
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks