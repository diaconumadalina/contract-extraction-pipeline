import json
from evaluation.heatmap import generate_heatmap

if __name__ == "__main__":
    doc_pairs = [
        (
            "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\expected"
            "\\contract_1.json",
            "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\results\\extracted\\extracted_1.json"
        )
    ]

    all_results = []

    for exp, pred in doc_pairs:
        expected = json.load(open(exp))
        predicted = json.load(open(pred))

        row = {k: int(expected[k] == predicted.get(k)) for k in expected}
        all_results.append(row)

    generate_heatmap(all_results)
