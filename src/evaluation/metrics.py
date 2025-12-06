def field_accuracy(expected: dict, predicted: dict):
    total = len(expected)
    correct = sum(1 for key in expected if expected[key] == predicted.get(key))
    return correct / total

def completeness(predicted: dict):
    total = len(predicted)
    filled = sum(1 for v in predicted.values() if v not in [None, "", "null"])
    return filled / total

