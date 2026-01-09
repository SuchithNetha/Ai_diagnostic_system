import os
import pandas as pd
import zipfile
from zenml import step

try:
    from zenml import step
    USE_ZENML = True
except ImportError:
    USE_ZENML = False


def load_csv(file_path: str) -> pd.DataFrame:
    """Load a single CSV file."""
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    print(f"[OK] Loaded CSV: {file_path}, shape={df.shape}")
    return df


def load_zip(file_path: str) -> pd.DataFrame:
    """Extract a zip file containing exactly one CSV & load it."""
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall("data/extracted/")  # extract to folder

    # find the extracted CSV
    extracted_files = [
        f for f in os.listdir("data/extracted/") if f.endswith(".csv")
    ]

    if not extracted_files:
        raise FileNotFoundError("No CSV found inside ZIP!")

    csv_path = os.path.join("data/extracted", extracted_files[0])
    print(f"[OK] Extracted {csv_path}")

    return load_csv(csv_path)


@step
def data_ingestion_step(file_path: str) -> pd.DataFrame:
    """Loads CSV or ZIP medical datasets."""
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        return load_csv(file_path)

    elif ext == ".zip":
        return load_zip(file_path)

    else:
        raise ValueError(f"Unsupported file type: {ext}")


if __name__ == "__main__":
    # TEST both types
    #data_ingestion_step("data/medical_data.csv")
   df= data_ingestion_step("data/medical_data.zip")
   ptint(df.head())