from src.extraction.extractor import ContractExtractor

sample_text = """
Contract Title: IT Services Agreement
Buyer: City Council of Springfield
Supplier: TechNova Solutions
Contract Value: $185,000
Start Date: Jan 1, 2024
End Date: Dec 31, 2024
"""

extractor = ContractExtractor()
result = extractor.extract(sample_text)

print(result)

