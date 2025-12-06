import json
from pathlib import Path
from src.loaders.document_loader import load_document
from src.preprocess.pipeline_preprocess import preprocess_text
from src.extraction.extractor import ContractExtractor


def extract_pdf_to_json(pdf_path: str, output_json_path: str):
    # 1. Load PDF text
    raw_text = load_document(pdf_path)

    # 2. Preprocess text (clean + chunking)
    chunks = preprocess_text(raw_text)

    extractor = ContractExtractor()
    results = []

    # 3. Extract from each chunk
    for chunk in chunks:
        result = extractor.extract(chunk)
        results.append(result.model_dump())

    # 4. Simplest merge strategy: keep first chunk result
    merged = results[0] if results else {}

    # 5. Save as JSON
    Path(output_json_path).parent.mkdir(parents=True, exist_ok=True)

    print(merged)

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2)

    print(f"Saved: {output_json_path}")


if __name__ == "__main__":
    extract_pdf_to_json(
        "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\data\\raw\\contracts\\narrative_contract_1.pdf",
        "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\results\\extracted\\extracted_1.json"
    )
