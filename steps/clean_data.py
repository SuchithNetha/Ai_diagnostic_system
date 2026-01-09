import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from zenml import step
from typing import Tuple  # <--- 1. ADD THIS IMPORT

@step
def clean_data(df: pd.DataFrame) -> Tuple[
    pd.DataFrame, 
    pd.DataFrame, 
    pd.Series, 
    pd.Series
]: # <--- 2. ADD THIS TYPE HINT
    logging.info("Cleaning data and encoding labels...")
    
    # Features (symptoms) and Target (disease)
    X = df.drop(columns=["disease"])
    y = df["disease"]

    # Label Encoding (Critical for Classification)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Split the data (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )
    
    # Return as a tuple of 4 items
    return X_train, X_test, pd.Series(y_train), pd.Series(y_test)