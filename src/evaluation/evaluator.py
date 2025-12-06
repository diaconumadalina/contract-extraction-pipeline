import json
from tabulate import tabulate
from evaluation.metrics import field_accuracy, completeness
from evaluation.similarity import semantic_similarity


def evaluate_pair(expected_path, predicted_path):
    expected = json.load(open(expected_path))
    predicted = json.load(open(predicted_path))

    table = []
    for field in expected:
        exp = expected[field]
        pred = predicted.get(field)

        if exp == pred:
            sim = 1.0
        else:
            sim = semantic_similarity(str(exp), str(pred)) if pred else 0.0

        table.append([field, exp, pred, sim])

    print(tabulate(table, headers=["Field", "Expected", "Predicted", "Semantic Sim"], tablefmt="fancy_grid"))

    print("\nField Accuracy:", field_accuracy(expected, predicted))
    print("Completeness:", completeness(predicted))
