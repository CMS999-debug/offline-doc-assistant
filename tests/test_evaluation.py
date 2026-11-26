from evaluate import evaluate


def test_baseline_accuracy_does_not_regress():
    assert evaluate() >= 0.6