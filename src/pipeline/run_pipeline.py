from src.loaders.document_loader import load_document
from src.preprocess.pipeline_preprocess import preprocess_text
from src.extraction.extractor import ContractExtractor


def run_pipeline(path: str):
    print(f"\n=== PROCESSING: {path} ===")

    raw = load_document(path)
    chunks = preprocess_text(raw)

    extractor = ContractExtractor()

    results = []
    for i, chunk in enumerate(chunks, 1):
        print(f"\n--- Extracting chunk {i}/{len(chunks)} ---")
        result = extractor.extract(chunk)
        results.append(result)

    return results
