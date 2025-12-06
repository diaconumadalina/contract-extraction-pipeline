# from src.extraction.extractor import ContractExtractor
from src.loaders.pdf_loader import load_pdf_text
from src.preprocess.pipeline_preprocess import preprocess_text


# test etapa 1
# sample_text = """
# Contract Title: IT Services Agreement
# Buyer: City Council of Springfield
# Supplier: TechNova Solutions
# Contract Value: $185,000
# Start Date: Jan 1, 2024
# End Date: Dec 31, 2024
# """
#
#
# def main():
#     # Initialize the extractor using config.toml
#     extractor = ContractExtractor()
#
#     # Run extraction on the sample text
#     result = extractor.extract(sample_text)
#
#     print("\n=== Extraction Result ===\n")
#     print(result.model_dump_json(indent=2))
#
#
# if __name__ == "__main__":
#     main()


# test etapa 2
# from src.loaders.pdf_loader import load_pdf_text
# from src.loaders.txt_loader import load_txt_text
# from pathlib import Path
#
#
# def test_pdf():
#     pdf_path = Path("data/raw/narrative_contract_3.pdf")
#     text = load_pdf_text(pdf_path, max_pages=2)
#     print("=== PDF TEXT SAMPLE ===")
#     print(text[:1000])
#
#
# def test_txt():
#     txt_path = Path("data/raw/test_contract.txt")
#     text = load_txt_text(txt_path)
#     print("=== TXT TEXT SAMPLE ===")
#     print(text[:1000])

# test etapa 3

def test_preprocess():
    raw = load_pdf_text("data/raw/contracts/messy_contract.pdf")
    chunks = preprocess_text(raw)

    print("Number of chunks:", len(chunks))
    for i, c in enumerate(chunks, 1):
        print(f"\n---- CHUNK {i} ----\n{c[:500]}\n")


if __name__ == "__main__":
    # test_pdf()
    # test_txt()
    test_preprocess()
