def chunk_pages(pages: list[dict], max_chars: int = 3000) -> list[dict]:
    """
    Split PDF page text into smaller chunks for LLM extraction and vector search.

    Each chunk keeps track of source page numbers.
    """
    chunks = []

    for page in pages:
        page_num = page["page"]
        text = page["text"]

        if not text:
            continue

        start = 0
        chunk_id = 1

        while start < len(text):
            chunk_text = text[start:start + max_chars]

            chunks.append(
                {
                    "chunk_id": f"page_{page_num}_chunk_{chunk_id}",
                    "page": page_num,
                    "text": chunk_text
                }
            )

            start += max_chars
            chunk_id += 1

    return chunks


if __name__ == "__main__":
    from extract_pdf import extract_text_from_pdf

    pages = extract_text_from_pdf("data/manuals/sample_manual.pdf")
    chunks = chunk_pages(pages)

    print(f"Created {len(chunks)} chunks.")
    print(chunks[0])