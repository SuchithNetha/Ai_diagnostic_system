import logging
import pandas as pd
from zenml import step
import zipfile

class DataIngestor:
    def __init__(self, import_path: str):
        self.import_path = import_path

    def get_data(self):
        logging.info(f"Ingesting data from {self.import_path}")
        with zipfile.ZipFile(self.import_path, 'r') as zip_ref:
            # This unzips and reads your medical_diagnosis.csv
            zip_ref.extractall("extracted_data")
        return pd.read_csv("extracted_data/medical_diagnosis.csv")

@step
def ingest_data(loader_path: str) -> pd.DataFrame:
    ingestor = DataIngestor(loader_path)
    df = ingestor.get_data()
    return df