import pytest
from src.model_utils import compute_accuracy, min_max_normalize


def test_compute_accuracy():
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 1, 0, 0]
    assert compute_accuracy(y_true, y_pred) == 0.8


def test_compute_accuracy_empty():
    with pytest.raises(ValueError):
        compute_accuracy([], [])


def test_min_max_normalize():
    vals = [10, 20, 30]
    normalized = min_max_normalize(vals)
    assert normalized == [0.0, 0.5, 1.0]
