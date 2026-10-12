"""
ML Utility functions for data evaluation and metric calculation.
"""


def compute_accuracy(y_true, y_pred):
    """Compute accuracy score between actual and predicted labels."""
    if len(y_true) == 0:
        raise ValueError("Input lists cannot be empty")
    if len(y_true) != len(y_pred):
        raise ValueError("Lengths of y_true and y_pred must match")
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    return correct / len(y_true)


def min_max_normalize(values):
    """Normalize numeric values to [0, 1] range."""
    if not values:
        return []
    min_v, max_v = min(values), max(values)
    if min_v == max_v:
        return [0.0] * len(values)
    return [(v - min_v) / (max_v - min_v) for v in values]
