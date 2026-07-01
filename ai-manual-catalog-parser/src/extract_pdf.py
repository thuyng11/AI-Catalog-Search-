import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extract text from each page of a PDF.

    Returns:
        A list of dictionaries:
        [
            {"page": 1, "text": "..."},
            {"page": 2, "text": "..."}
        ]
    """
    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    document = fitz.open(pdf_path)
    pages = []

    for page_num, page in enumerate(document, start=1):
        text = page.get_text("text")

        pages.append(
            {
                "page": page_num,
                "text": text.strip()
            }
        )

    document.close()
    return pages


if __name__ == "__main__":
    sample_pdf = "data/manuals/sample_manual.pdf"
    extracted_pages = extract_text_from_pdf(sample_pdf)

    for page in extracted_pages[:3]:
        print(f"\n--- Page {page['page']} ---")
        print(page["text"][:1000])