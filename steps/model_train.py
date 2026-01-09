from zenml import step
from src.model_dev import RandomForestStrategy
import pandas as pd
@step
def train_model(X_train: pd.DataFrame, y_train: pd.Series):
    strategy = RandomForestStrategy()
    model = strategy.build_and_train_model(X_train, y_train)
    return model