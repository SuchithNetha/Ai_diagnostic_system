import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from zenml import step

@step
def clean_data(df: pd.DataFrame):
    logging.info("Cleaning medical data and encoding labels.")
    
    # 1. Define Features (symptoms) and Target (disease)
    X = df.drop(columns=["disease"])
    y = df["disease"]

    # 2. Encode Disease Names (e.g., 'Covid' -> 1)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # 3. Train-Test Split (The 'Ayush' logic: 80/20 split)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )
    
    return X_train, X_test, pd.Series(y_train), pd.Series(y_test)