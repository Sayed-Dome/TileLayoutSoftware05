import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(data: np.ndarray) -> RandomForestClassifier:
    """
    Train a machine learning model on the tile layout data.

    Args:
        data: Tile layout data

    Returns:
        RandomForestClassifier: Trained machine learning model
    """
    X = data[:, :-1]
    y = data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_model(model: RandomForestClassifier, data: np.ndarray) -> np.ndarray:
    """
    Use the trained machine learning model to make predictions on new tile layout data.

    Args:
        model: Trained machine learning model
        data: New tile layout data

    Returns:
        np.ndarray: Predictions made by the machine learning model
    """
    return model.predict(data)
