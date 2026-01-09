from pipelines.training_pipeline import train_pipeline
import logging
import pandas as pd
if __name__ == "__main__":
    # Define the path to your medical data
    DATA_PATH = "data/medical_data.zip"

    logging.info("Starting the Medical Diagnosis Training Pipeline...")
    
    # Trigger the ZenML Pipeline
    # This calls all your steps: Ingest -> Clean -> Train -> Evaluate
    train_pipeline(data_path=DATA_PATH)

    logging.info("Pipeline execution completed successfully.")
    logging.info("To see your results, run: 'mlflow ui' in your terminal.")