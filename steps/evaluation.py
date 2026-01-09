import logging
from sklearn.metrics import accuracy_score
from zenml import step
import pandas as pd
@step
def evaluation(model, X_test: pd.DataFrame, y_test: pd.Series) -> float:
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)
    logging.info(f"Model Accuracy: {accuracy}")
    return accuracy