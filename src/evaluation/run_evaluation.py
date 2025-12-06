from evaluation.evaluator import evaluate_pair

# List of (expected, predicted) JSON pairs
files = [
    (
        "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\expected\\contract_1.json",
        "C:\\Users\\Madalina Diaconu\\PycharmProjects\\contract-extraction-pipeline\\src\\evaluation\\results\\extracted\\extracted_1.json",
    ),
    # Add more if needed:
    # ("evaluation/expected/contract_2.json", "evaluation/results/extracted/extracted_2.json"),
]

if __name__ == "__main__":
    for exp, pred in files:
        print(f"\n=== Evaluating {pred} ===")
        evaluate_pair(exp, pred)
