import numpy as np


def predict_input(model, X_test_scaled):
    """
    Given a model and test data, predict the target values.

    Args:
    - model: The trained machine learning model
    - X_test_scaled: The scaled test data for prediction

    Returns:
    - y_pred: The predicted target values
    """
    y_pred = model.predict(X_test_scaled)
    return y_pred
